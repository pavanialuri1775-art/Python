#we can change the value of a specific item by referring to its key name
#change the year to 2023
thisdict={"college":"gnit",
          "place":"ibp",
          "year":2026
}
thisdict["year"]=2023
print(thisdict)#{'college': 'gnit', 'place': 'ibp', 'year': 2023}

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
thisdict = {
  "brand": "puma",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)#{'brand': 'puma', 'year': 2020}



