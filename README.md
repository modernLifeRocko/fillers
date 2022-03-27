# Anime Filler Project

Info from www.animefillerlist.com in some convenient formats: .csv and .json 

### animefillerlist.csv
Contains the most of the info on the site in the form:

show, episode number, episode title, type (filler/canon), release date

### animefillerlist.json

Map  with keys = show names, and values given by objects of the form:
{
  'Release': Date,
  'episode Type': [list of episodes of the given type]
}

### site data format
Release dates are in the format YYYY-MM-DD.
episode type is one of: 'Manga Canon', 'Anime Canon', 'Filler', 'Mixed'...
(There might be others, I'm unsure if the site forces the info submissions to follow that pattern)

### anifiller.py
I have added the code I use to get the data. If you need the information in a different format, modify this code accordingly.
