#! python3
import numpy as np
import matplotlib.pyplot as plt
import json
import re

animes = json.loads(open('../data/animefillerlist.json', 'r').read())

# Get a list of years and filler percentage
percents = np.array([])
years = np.array([])

for ani in animes:
  if not animes[ani]["Release"]:
    continue
  year = int(re.findall(r'^\d{4}', animes[ani]["Release"])[0])
  years = np.append(years, year)
  total_eps = 0
  filler_eps = 0
  for key in animes[ani]:
    if key == 'Release': continue
    total_eps += len(animes[ani][key])
    if (re.search('[Cc]anon', key) is not None) and (re.search('[Ff]iller', key) is not None):
      filler_eps += 0.5*len(animes[ani][key])
    elif re.search('[Cc]anon', key) is None:
      filler_eps = len(animes[ani][key])
  if filler_eps/total_eps == 1:
    print(ani)
  percents = np.append(percents, 100 * filler_eps/total_eps)


plt.scatter(years, percents)
plt.xlabel('Years')
plt.ylabel('Filler percentage')

# Linear regression to estimate filler evolution

a, b = np.polyfit(years, percents, 1)

# years = sorted(years)
plt.plot(years, a*years+b, color='red')


plt.savefig('../images/plot_evolution.png')

plt.show()
