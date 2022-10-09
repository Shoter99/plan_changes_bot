#!/usr/bin/env python3

from main import check_for_changes
import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@tasks.loop(minutes=60)
async def send_announcement():
    print('Checking for news')
    channel = client.get_channel(1027940214523564042)
    latest = check_for_changes()
    if latest != False:
        msg = f"""
            Nowa zmiana!\n
            {latest[0]}\n
            {latest[1]}\n
            {latest[2]}\n
            {latest[3]}\n
            {latest[4]}\n

            """
        await channel.send(msg)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    send_announcement.start()

if "__main__" == __name__:
    client.run(TOKEN)

