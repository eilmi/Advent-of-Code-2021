from collections import Counter
import numpy as np
import re

f = open("input.txt").readlines()

polymere=f[0].strip()

rules=[]

for i in f[2:]:
    rules.append(i.strip().split(" -> "))

rules=np.array(rules)

rules = dict(zip(rules[:,0],rules[:,1]))

def getnewpolymere(polymere):
    newpolymere=""
    for i in range(0,len(polymere)-1):
        newpolymere+=polymere[i]
        pair=polymere[i:i+2]
        if pair in rules:
            newpolymere+=rules.get(pair)

    newpolymere+=polymere[-1]
    return newpolymere
        

for i in range(40):
    polymere=getnewpolymere(polymere)
    print(i)
    #print(polymere)

mostcom = Counter(c.lower() for c in re.findall(r"\w", polymere)).most_common()[0]
leastcom = Counter(c.lower() for c in re.findall(r"\w", polymere)).most_common()[-1]

print(mostcom[1]-leastcom[1])