import re
import json
from pprint import pprint

import xml.etree.ElementTree as ET



with open("newsafr.json", encoding="utf-8") as f:
  data = f.read()

wordreg = re.compile('\"(description|title)\": \"(.*)\"')

data = [i[1].lower() for i in wordreg.findall(data)]


data = ' '.join(data).split(' ')

frequent = {}

for word in data:
  if len(word) > 6:
    if word in frequent:
      frequent[word] += 1
    else:
      frequent[word] = 1

frequent = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
frequent = frequent[:10]

print('RE')

for pair in frequent:
  print(f'{pair[0]} - {pair[1]}')

with open('newsafr.json') as fin:
  data = json.load(fin)

print(data['rss']['channel']['items'][0]['description'])
frequent = {}
for i in data['rss']['channel']['items']:
  for word in i['description'].lower().split(' '):
    if len(word) > 6:
      if word in frequent:
        frequent[word] += 1
      else: 
        frequent[word] = 1

for i in data['rss']['channel']['items']:
  for word in i['title'].lower().split(' '):
    if len(word) > 6:
      if word in frequent:
        frequent[word] += 1
      else: 
        frequent[word] = 1

frequent = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
frequent = frequent[:10]

print('JSON')
for pair in frequent:
  print(f'{pair[0]} - {pair[1]}')

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

xml_items = root.findall("channel/item/description")

frequent = {}

for i in xml_items:
  for word in i.text.lower().split(' '):
    if len(word) > 6:
      if word in frequent:
        frequent[word] += 1
      else: 
        frequent[word] = 1

xml_items = root.findall("channel/item/title")

for i in xml_items:
  for word in i.text.lower().split(' '):
    if len(word) > 6:
      if word in frequent:
        frequent[word] += 1
      else: 
        frequent[word] = 1

frequent = sorted(frequent.items(), key=lambda x: x[1], reverse=True)
frequent = frequent[:10]

print('XML')
for pair in frequent:
  print(f'{pair[0]} - {pair[1]}')
