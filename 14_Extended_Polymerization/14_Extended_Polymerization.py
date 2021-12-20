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

values={}

for i in range(len(polymere)-1):
    st=polymere[i:i+2]
    values.update({st:values.get(st,0)+1})

characters={}

for i in range(len(polymere)):
    characters.update({polymere[i]:characters.get(polymere[i],0)+1})



for iters in range(40):
    update={}
    for x in values:
        hm = values.get(x)
        if hm==0:
            continue
        else:
            newchar = rules.get(x,"")
            if newchar=="":
                continue
            lastcharcount = characters.get(newchar,0)
            characters.update({newchar:lastcharcount+hm})
            update.update({x:update.get(x,0)-hm})
            newv1=x[0]+newchar
            newv2=newchar+x[1]
            update.update({newv1:update.get(newv1,0)+hm,newv2:update.get(newv2,0)+hm})

    for i in update:
        hm=update.get(i,0)

        values.update({i:values.get(i,0)+hm})


print(max(characters.values())-min(characters.values()))
