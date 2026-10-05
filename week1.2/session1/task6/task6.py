# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
musics = {
    "benjamin_grey": [["animefantastic", "rao nuke", "signed"], ["1984", "1990", "1066"]],
    "chaplain": [["i can do it carmen", "save ncorp", "warden"], ["1789", "2098", "1999"]],
    "oanc": [["loner", "worst company", "mcve"], ["2016", "2018", "2020"]]
}

# Pretty-print the data structure
pprint(musics)

# Display details of one album recorded by a specific artist
pprint(musics["benjamin_grey"])

num = 0
for i in musics:
    for x in musics[i][0]:
        num = num + 1
print(num)