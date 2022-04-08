#! python3
#find anime fillers

import requests as req
import bs4, csv, json


res = req.get('https://www.animefillerlist.com/shows')
soup = bs4.BeautifulSoup(res.text,'html.parser')
animeList = soup.select('#ShowList .Group li a')

#CSV file setup
outputFile = open('animefillerlist.csv','w', newline='')
outputWriterCSV = csv.writer(outputFile)
outputWriterCSV.writerow(['Show', 'Episode', 'Title', 'Type', 'Release'])

#JSON file setup
#outputListJSON = open('animefillerlist.json','w')
animeDict = {}
types = []


for anime in animeList:
  animeName = anime.text
  animeRes = req.get('https://www.animefillerlist.com'+anime.get('href'))
  animeRes.raise_for_status()
  epsList = bs4.BeautifulSoup(animeRes.text,'html.parser').select('table.EpisodeList tbody tr')
  if epsList == []: continue

  releaseYear =epsList[0].select('.Date')[0].getText()
  animeDict[animeName] = {}
  animeDict[animeName]['Release'] = releaseYear
  for type in types:
    animeDict[animeName][type]=[]
  
  for ep in epsList:
    epTitle = ep.select('.Title')[0].getText()
    epNumber = int(ep.select('.Number')[0].getText())
    epType = ep.select('.Type')[0].getText()
    if not epType in types:
      types.append(epType)
      animeDict[animeName][epType]=[]
    epDate = ep.select('.Date')[0].getText()
    
    animeDict[animeName][epType].append(epNumber)
    outputWriterCSV.writerow([animeName, epNumber, epTitle, epType, epDate])

with open('animefillerlist.json','w') as outJson:
  json.dump(animeDict, outJson)

outputFile.close()
#outputListJSON.close()

print(types)    
    

#preemptively useful function to search for the episodes list without having the full name of the show
def get_eps(name):
  #find the page of the anime in animefillers.com
  res = req.get('https://www.animefillerlist.com/search/node/'+name)
  res.raise_for_status()
  name = bs4.BeautifulSoup(res.text,'html.parser').select('.search-result a')[0].get('href')

  #find the episodes list
  page = bs4.BeautifulSoup(req.get(name), 'html.parser')
  eps = page.select('table.EpisodeList tr')#each row in the table corresponds to one ep
  return eps

