import numpy as np

li = open("demo.txt").readlines()
import sys
sys.setrecursionlimit(2000)

cavern=[]

for i in li:
    line=[]
    i=i.strip()

    for t in i:
        line.append(t)
    cavern.append(line)


cavern=np.array(cavern,dtype=int)

path_risk_levels=[]

risk_levels=np.zeros(cavern.shape)

def nextpos(coordinates,risklevel):

    if risk_levels[coordinates[0],coordinates[1]] != 0 and risk_levels[coordinates[0],coordinates[1]] <= risklevel:
        return
    risk_levels[coordinates[0],coordinates[1]]=risklevel
    risklevel+=cavern[coordinates[0],coordinates[1]]
    if cavern.shape[0]-1 == coordinates[0] and cavern.shape[1]-1 ==coordinates[1]:
        path_risk_levels.append(risklevel)
        return
    
    if cavern.shape[0]-1 > coordinates[0]:
        nextpos([coordinates[0]+1,coordinates[1]],risklevel)
    if cavern.shape[1]-1 > coordinates[1]:
        nextpos([coordinates[0],coordinates[1]+1],risklevel)

nextpos([0,0],-cavern[0,0])

print(min(path_risk_levels))

#print(cavern)

############### Part Two ########################

def addonetoarray(array,value,wrapvalue):
    array+=1
    ind=np.where(array>wrapvalue)
    for i in range(len(ind[0])):
        array[ind[0][i],ind[1][i]]=1
    return array


newcavern=cavern.copy()
for i in range(4):
    newcavern=addonetoarray(newcavern,1,9)
    cavern=np.concatenate((cavern,newcavern),axis=1)

newcavern=cavern.copy()
for i in range(4):
    newcavern=addonetoarray(newcavern,1,9)
    cavern=np.concatenate((cavern,newcavern),axis=0)


path_risk_levels=[]

risk_levels=np.zeros(cavern.shape)

nextpos([0,0],-cavern[0,0])

print(min(path_risk_levels))



#2837 is too high