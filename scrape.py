import requests
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv
load_dotenv()

class Player:
  def __init__(self, name, age, birthday, salary, value, weapon, aim, teamplay, handling, playing_iq, quickness, determination, awareness, creativity, patience, calmness, total, leadership, experience, stamina, talent):
    self.name = name
    self.age = age
    self.birthday = birthday
    self.salary = salary
    self.value = value
    self.weapon = weapon
    self.aim = aim
    self.teamplay = teamplay
    self.handling = handling
    self.playing_iq = playing_iq
    self.quickness = quickness
    self.determination = determination
    self.awareness = awareness
    self.creativity = creativity
    self.patience = patience
    self.calmness = calmness
    self.total = total
    self.leadership = leadership
    self.experience = experience
    self.stamina = stamina
    self.talent = talent
  
  def __repr__(self):  
    return "%s %s" % (self.aim, self.name)  


headers = {
    'Origin': 'http://fiddle.jshell.net',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

c = {
  'lang': os.getenv('LANG'),
  'login':	os.getenv('LOGIN'),
  'PHPSESSID':	os.getenv('PHPSESSID'),
  'prefs':	os.getenv('PREFS'),
  'session-test':	os.getenv('SESSION_TEST'),
  'sid': os.getenv('SID')
}

root_url = 'https://www.cs-manager.com'

def get_players_on_page(page_url):
  transfer_page = requests.get(root_url + page_url, headers=headers, cookies=c)
  soup = BeautifulSoup(transfer_page.text, 'html.parser')
  players_on_page = soup.find_all('article')
  
  players = []
  # transfer_list_url
  # special
  for p in players_on_page:
    name = p.select_one('div.first-col > ul > li:nth-child(1)').text.replace('Name:','')
    age = p.select_one('div.first-col > ul > li:nth-child(2)').text.replace('Age: ','').replace(' years', '')
    birthday = p.select_one('div.first-col > ul > li:nth-child(3)').text.replace('Birthday:Day ','')
    salary = p.select_one('div.second-col > ul > li:nth-child(1)').text.replace('Salary:','').replace(' csm','').replace(' ', '')
    value = p.select_one('div.second-col > ul > li:nth-child(2)').text.replace('Value:','').replace(' ', '')
    weapon = p.select_one('div.second-col > ul > li:nth-child(3)').text.replace('Weapon: ','')
    aim = p.select_one('ul.skills-bar > li:nth-child(1) > div.visual').text.replace(' ', '').split('/', 1)[0]
    teamplay = p.select_one('ul.skills-bar > li:nth-child(2) > div.visual').text.replace(' ', '').split('/', 1)[0]
    handling = p.select_one('ul.skills-bar > li:nth-child(3) > div.visual').text.replace(' ', '').split('/', 1)[0]
    playing_iq = p.select_one('ul.skills-bar > li:nth-child(4) > div.visual').text.replace(' ', '').split('/', 1)[0]
    quickness = p.select_one('ul.skills-bar > li:nth-child(5) > div.visual').text.replace(' ', '').split('/', 1)[0]
    determination = p.select_one('ul.skills-bar > li:nth-child(6) > div.visual').text.replace(' ', '').split('/', 1)[0]
    awareness = p.select_one('ul.skills-bar > li:nth-child(7) > div.visual').text.replace(' ', '').split('/', 1)[0]
    creativity = p.select_one('ul.skills-bar > li:nth-child(8) > div.visual').text.replace(' ', '').split('/', 1)[0]
    patience = p.select_one('ul.skills-bar > li:nth-child(9) > div.visual').text.replace(' ', '').split('/', 1)[0]
    calmness = p.select_one('ul.skills-bar > li:nth-child(10) > div.visual').text.replace(' ', '').split('/', 1)[0]
    total = p.select_one('ul.skills-bar > li:nth-child(11)').text.replace('Total:', '').replace(' ', '').split('/', 1)[0]
    leadership = p.select_one('div.exp > ul > li:nth-child(1) > img')['src'].replace('/images/experience_', '').replace('.png', '')
    experience = p.select_one('div.exp > ul > li:nth-child(2) > img')['src'].replace('/images/experience_', '').replace('.png', '')
    stamina = p.select_one('div.talent > ul > li:nth-child(1) > img')['src'].replace('/images/run_bar_', '').replace('.png', '')
    talent = p.select_one('div.talent > ul > li:nth-child(2) > img')['src'].replace('/images/star_bar_', '').replace('.png', '')
    
    players.append(Player(name, age, birthday, salary, value, weapon, aim, teamplay, handling, playing_iq, quickness, determination, awareness, creativity, patience, calmness, total, leadership, experience, stamina, talent))
  
  return players

transfer_page = requests.get(root_url + '/csm/?p=office_transfer&start=0', headers=headers, cookies=c)
soup = BeautifulSoup(transfer_page.text, 'html.parser')
transfer_page_anchors = soup.find(id='date-nav').find_all('a', href=True)

players = []

# remove last element in array as this is page 0 again (causing duplicates)
transfer_page_anchors.pop()
for anchor in transfer_page_anchors:
  players += get_players_on_page(anchor['href'])
  break

with open('data/data.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow([
    'name',
    'age',
    'birthday',
    'salary',
    'value',
    'weapon',
    'aim',
    'teamplay',
    'handling',
    'playing_iq',
    'quickness',
    'determination',
    'awareness',
    'creativity',
    'patience',
    'calmness',
    'total',
    'leadership',
    'experience',
    'stamina',
    'talent'
  ])

  for p in players:
    writer.writerow([
      p.name,
      p.age,
      p.birthday,
      p.salary,
      p.value,
      p.weapon,
      p.aim,
      p.teamplay,
      p.handling,
      p.playing_iq,
      p.quickness,
      p.determination,
      p.awareness,
      p.creativity,
      p.patience,
      p.calmness,
      p.total,
      p.leadership,
      p.experience,
      p.stamina,
      p.talent
    ])