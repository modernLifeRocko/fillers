# Anime Filler Project
Do modern day anime have more fillers than the older ones? 
This question is the central focus of this project.

## Obtaining the data
The data comes from the site www.animefillerlist.com, and converted to some convenient formats: .csv and .json 

### animefillerlist.csv
Contains the most of the info on the site in the form:

show, episode number, episode title, type (filler/canon), release date

This file is not used for the analysis, but it seemed generally useful to have.

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
I have added the code I use to scrape the data. If you need the information in a different format, modify this code accordingly.

## Analysis

So far the analysis consists of s scatter plot and linear regression.

## Concerns
The results of this study might not be representative of the actual trend of filler in anime in general. There are at least two reasons for this:

1. The selection of anime in animefillerlist is by no means a complete list of anime, and it has far more information on recent years. This might make it so that there is a more prevalence of filler in recent anime, as the older anime included in the list are likely "classics".  However, it looked like the best option.

2. Also, long duration anime are treated as a single data point. This might skew the balance in the opposite direction, as all later filler episodes will be considered in the first year, which usually has the least amount of filler. 
