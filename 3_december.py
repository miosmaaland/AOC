import re
from collections import defaultdict

totalt = 0
brett = []
gir_numre = defaultdict(list)

def vurder_tallnaboer(start_y, start_x, end_y, end_x, num):
    global gir_numre
    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            if 0 <= y < len(brett) and 0 <= x < len(brett[y]):
                if brett[y][x] not in '0123456789.':
                    if brett[y][x] == '*':
                        gir_numre[(y, x)].append(num)
                    return True
    return False

tall_mønster = re.compile('\d+') # finner tall

with open('dec3') as fil:  # åpner filen
    for linje in fil.readlines(): # leser linje for linje
        brett.append(linje.strip()) # legger til linjen i brettet

for rad_num in range(len(brett)):
    for match in re.finditer(tall_mønster, brett[rad_num]):
        if vurder_tallnaboer(rad_num-1, match.start()-1, rad_num+1, match.end(), int(match.group(0))): 
            totalt += int(match.group(0))

print(totalt)

totalt = 0
for k, v in gir_numre.items():
    if len(v) == 2:
        totalt += v[0] * v[1] #Ganger sammen de to tallene som blir funnet i listen
print(totalt)


