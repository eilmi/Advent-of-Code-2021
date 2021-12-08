import numpy as np

f = open("input.txt").readlines()

craps=f[0].strip().split(",")
craps = np.array(craps,dtype=int)

minimum=min(craps)
maximum=max(craps)

partone=[]
parttwo=[]
f = lambda x: (x ** 2 + x)/2 # define function which will be mapped onto numpy array

for i in range(minimum,maximum+1): # iterate over all possible horizontal lines
    t=np.absolute(craps-i) # calculate distance between all craps and current horizontal line
    partone.append(t.sum()) # append sum of all distances to array
    t=f(t) # map function over all distances for part two
    parttwo.append(int(t.sum()))

print("Part one:",min(partone))
print("Part two:",min(parttwo))
