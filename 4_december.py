#03.12.2023 - Lottosammentreff


linjer = open('input4', 'r').readlinjer()

def part1():
    total = 0 #Lager variabel som vi setter lik null
    for linje in linjer: #Går gjennom linjene
        x, y = map(str.split, linje.split('|')) #Splitter linjen i to
        treff = set(x) & set(y) #Finner alle treff mellom x og y 
       
        total += 2 ** (len(treff) - 1) if treff else 0   #Finner antall treff og legger til 2^(antall treff - 1) i total
    return total

def part2():
    kort = [1] * len(linjer) #Lager en liste med ener som er like lang som antall linjer
    for i, linje in enumerate(linjer): #Går gjennom linjene
        x, y = map(str.split, linje.split('|')) #Splitter linjen i to
        n = len(set(x) & set(y)) #Finner antall treff mellom x og y
        for j in range(i + 1, min(i + 1 + n, len(linjer))): #Går gjennom alle linjene etter linje i
            kort[j] += kort[i] #Legger til antall treff i kortet
    return sum(kort) #Summerer alle tallene i kortet

print(part1(), part2()) #Printer ut resultatene fra part1 og part2