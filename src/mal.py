import requests as req
import bs4


def get_page(name):
  # guarantees that name meets MAL size of search terms restrictions.
  if len(name) < 3:
    name = name + '   '
  elif len(name) >= 100:
    name = name[:100]

  res = req.get('https://myanimelist.net/search/all?cat=all&q='+name)
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  return soup.select('article .list .information .title a.hoverinfo_trigger')[0]['href']


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
