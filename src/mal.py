import requests as req
import bs4
from Levenshtein import distance as levd
import numpy as np


def get_page(name):
  # guarantees that name meets MAL size of search terms restrictions.
  fname = name.lower()
  if len(name) < 3:
    name = name + '   '
  elif len(name) >= 100:
    name = name[:100]

  res = req.get('https://myanimelist.net/search/all?cat=anime&q='+name)
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  an_ress = soup.select('article .list .information .title a.hoverinfo_trigger')
  # find the search result closer in the Levenshtein distance
  mi = np.argmin([levd(fname, a.text.strip().lower()) for a in an_ress])
  return an_ress[mi]['href']


def get_rating(page):
  res = req.get(page)
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  return float(soup.select('.score-label')[0].contents[0])


def get_sequel(page):
  res = req.get(page)
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  rel_lst = soup.select('.related-entries .entry')
  for it in rel_lst:
    try:
      relation = it.select('.relation')[0]
      title = it.select('.title a')[0]
    except:
      continue

    if 'Sequel' in relation.contents[0]:
      return title['href']
