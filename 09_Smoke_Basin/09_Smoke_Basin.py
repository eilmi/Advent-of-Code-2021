import numpy as np

f = open("input.txt").readlines()
#f = open("demo.txt").readlines()

heightmap=[]
for row in f:
    row=row.strip()
    rows=[]
    #print(row)
    for point in row:
        #print(point)
        rows.append(point)
    heightmap.append(rows)

nparray=np.array(heightmap,dtype=int)


result=[]
for y in range(nparray.shape[0]):
    for x in range(nparray.shape[1]):
        minimas=[]
        if (y>=1):
            minimas.append(nparray[y-1][x])
        if(y<(nparray.shape[0])-1):
            minimas.append(nparray[y+1][x])
        if (x>=1):
            minimas.append(nparray[y][x-1])
        if (x<(nparray.shape[1])-1):
            minimas.append(nparray[y][x+1])
        
        if min(minimas)>nparray[y][x]:
            result.append(nparray[y][x])

print(result)
result=np.array(result)

print("Part one:",sum(result+1))

############ Part Two #####################

def checkneighbours(x,y):
    
