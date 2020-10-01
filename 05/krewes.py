#Dragos Lup, Ryan Ma, Jeffery Huang
#SoftDev
#K05 -- Teamwork, but Better This Time
#2020-09-28
import random
KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}
#Final version, first takes just the values from KREWES (the three lists), and turns that into a list.
#Then it randomly chooses between the three lists, and then it randomly chooses between all the values in the list.
print(random.choice(random.choice(list(KREWES.values()))))

#First version, creates a list of the keys and plugs a random one into KREWES, and then takes a random choice from there
#listo = []
#for x in KREWES.keys():
#    listo.append(x)
#print(random.choice(KREWES[random.choice(listo)]))

#Second version, makes one super big list with every value, and randomly chooses between all of them.
#listo = []
#for x in KREWES.values():
#    for y in x:
#        listo.append(y)
#print(random.choice(listo)
#After we realized we can use .values() we saw that we cna just use that instead of the rest of the complex stuff.
