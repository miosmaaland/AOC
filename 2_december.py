

import math
from collections import defaultdict
import re



with open("input") as fila:
    fil = fila.read().strip().split("\n")

kombinasjoner = 0
potensen = 0 

for f in fil : 
    deler = re.sub("[;,:]", "", f).split()

    maks_fargeantall = defaultdict (int)   #Slipper å lage nye keys hele tiden, blir laget dersom den ikke er tilstede
    for count , farge in zip(deler[2::2] , deler[3::2]):           #Begynner på tredje element, hopper med to ´/ Begynner på fjerde element, hopper med to
        maks_fargeantall[farge] = max(maks_fargeantall[farge], int(count))

    potens = math.prod(maks_fargeantall.values())  #Ganger sammen elementene i input-filen for å nærme oss en løsning


    if maks_fargeantall["red"] <= 12 and maks_fargeantall["green"] <= 13 and maks_fargeantall["blue"] <= 14:   # Sjekker at det ikke er mer enn vi ønsker av de forskjellige
        kombinasjoner += int(deler[1])

    potensen += potens




print(kombinasjoner)

print(potensen)







    












