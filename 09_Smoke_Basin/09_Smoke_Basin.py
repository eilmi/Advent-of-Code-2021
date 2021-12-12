import numpy as np
from numpy.core.fromnumeric import prod

f = open("input.txt").readlines()
#f = open("demo.txt").readlines()

heightmap=[]
for row in f:
    row=row.strip()
    rows=[]
    for point in row:
        rows.append(point)

    heightmap.append(rows)

nparray=np.array(heightmap,dtype=int) # convert into integer numpy array


minimalocations=[]
for y in range(nparray.shape[0]):
    for x in range(nparray.shape[1]):
        neighborhood=[]
        if (y>=1): # check if there is at least one position to the left available
            neighborhood.append(nparray[y-1][x])
        if(y<(nparray.shape[0])-1):
            neighborhood.append(nparray[y+1][x])
        if (x>=1):
            neighborhood.append(nparray[y][x-1])
        if (x<(nparray.shape[1])-1):
            neighborhood.append(nparray[y][x+1])
        
        if min(neighborhood)>nparray[y][x]:
            minimalocations.append([x,y])

minimavalues=[]
for i in minimalocations:
    minimavalues.append(nparray[i[1],i[0]]) # get height of all found low points 

minimavalues=np.array(minimavalues)

print("Part one:",sum(minimavalues+1))

############ Part Two #####################



checked=[]
def checknearby(x,y):
    global checked
    sum=1
    checked.append([x,y])
    if nparray[y,x]==9: # if height of current position is 9 return 0 because '9' doesn't count as being in a basin
        return 0
    if (y>=1) and [x,y-1] not in checked: # check if position to the left exists and wasn't checked before
        sum+=checknearby(x,y-1)
    if (y<(nparray.shape[0])-1) and [x,y+1] not in checked: # check if position to the right exists and wasn't checked before
        sum+=checknearby(x,y+1)
    if (x>=1) and [x-1,y] not in checked: # check if position to the right exists and wasn't checked before
        sum+=checknearby(x-1,y)
    if (x<(nparray.shape[1])-1) and [x+1,y] not in checked: # check if position below current one exists and wasn't checked before
        sum+=checknearby(x+1,y)

    return sum

basins=[]
for i in minimalocations: #iterate over all previously found local minimums
    basins.append(checknearby(i[0],i[1]))


print("Part two:",prod(sorted(basins,reverse=True)[0:3])) # sort after size, reverse sorted list, multiply the first 3 elements together


    