#! python3
import numpy as np
import matplotlib.pyplot as plt
import json
import re

animes = json.loads(open('../data/animefillerlist.json', 'r').read())

# Get a list of years and filler percentage
percents = np.array([])
years = np.array([])
lengths = np.array([])
ratings = np.array([])

for ani in animes:
  if not animes[ani]["Release"]:
    continue
  year = int(re.findall(r'^\d{4}', animes[ani]["Release"])[0])
  years = np.append(years, year)
  rating = animes[ani]["rating"]
  ratings = np.append(ratings, rating)
  total_eps = 0
  filler_eps = 0
  for key in animes[ani]:
    if key == 'Release' or key == 'rating': continue
    total_eps += len(animes[ani][key])
    if (re.search('[Cc]anon', key) is not None) and (re.search('[Ff]iller', key) is not None):
      filler_eps += 0.5*len(animes[ani][key])
    elif re.search('[Cc]anon', key) is None:
      filler_eps = len(animes[ani][key])
  if filler_eps/total_eps == 1:
    print(ani)
  percents = np.append(percents, 100 * filler_eps/total_eps)
  lengths = np.append(lengths, total_eps)

# Year vs Percentage of filler
figTvP, axTvP = plt.subplots()
axTvP.scatter(years, percents)
axTvP.set_xlabel('Release Year')
axTvP.set_ylabel('Filler percentage')

# Linear regression to estimate filler evolution

a, b = np.polyfit(years, percents, 1)
axTvP.plot(years, a*years+b, color='red')


figTvP.savefig('../images/plot_evolution.png')

# Year vs length of anime
figTvL, axTvL = plt.subplots()
axTvL.scatter(years, lengths)
axTvL.set_xlabel('Years')
axTvL.set_ylabel('Length of anime (episodes)')

a, b = np.polyfit(years, lengths, 1)
axTvL.plot(years, a*years+b, color='red')

figTvL.savefig('../images/length_evo.png')

# Length vs filler percentage
figLvP, axLvP = plt.subplots()
axLvP.scatter(lengths, percents)
axLvP.set_xlabel('Length of anime (episodes)')
axLvP.set_ylabel('Filler percentage')

a, b = np.polyfit(lengths, percents, 1)
axLvP.plot(lengths, a*lengths+b, color='red')

figLvP.savefig('../images/length_percentage.png')

# Quality vs filler percentage
figQvP, axQvP = plt.subplots()
axQvP.scatter(ratings, percents)
axQvP.set_xlabel('Anime rating')
axQvP.set_ylabel('Filler percentage')

a, b = np.polyfit(ratings, percents, 1)
axQvP.plot(ratings, a*ratings+b, color='red')

figQvP.savefig('../images/quality_percentage.png')

plt.show()
