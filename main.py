import requests
from bs4 import BeautifulSoup as bs

def write_to_file(annoucement):
    with open('last_annoucement.txt', 'w') as f:
        f.write(annoucement)


def read_from_file():
    with open('last_annoucement.txt', 'r') as f:
        line = f.readline()
    return line

def check_for_changes():
    URL = 'https://inf.ug.edu.pl/plan/index.php'
    r = requests.get(URL)
    soup = bs(r.content, 'html5lib')

    table = soup.find('tbody')
    announcements = []



    for row in table.findAll('tr', attrs = {'class':'tr'}):
        announcement = []
        for info in row.findAll('td'):
            announcement.append((info.text).strip())
        if 'informatyka (P): I rok' in  announcement[0]:
            announcements.append(announcement)
    last_announcement = " ".join(announcements[0])
    if read_from_file() != last_announcement:
        write_to_file(last_announcement)
        return announcements[0]
    return False 
