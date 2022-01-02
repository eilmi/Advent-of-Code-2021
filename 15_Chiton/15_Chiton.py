import numpy as np

li = open("input.txt").readlines()
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(200000)
cavern=[]

for i in li:
    line=[]
    i=i.strip()

    for t in i:
        line.append(t)
    cavern.append(line)


cavern=np.array(cavern,dtype=int)

path_risk_levels=[]

minrisk_level=99999999999999999

risk_levels=np.zeros(cavern.shape)

def nextpos(oldcoords,coordinates,risklevel,wherefrom):
    global minrisk_level
    global risk_levels
    
    
    risklevel+=cavern[coordinates[0],coordinates[1]]

    if risklevel>=minrisk_level:
        return

    if risk_levels[coordinates[0],coordinates[1]] != 0 and risk_levels[coordinates[0],coordinates[1]] <= risklevel:
        return

    

    risk_levels[coordinates[0],coordinates[1]]=risklevel
    if cavern.shape[0]-1 == coordinates[0] and cavern.shape[1]-1 ==coordinates[1]:
        if risklevel<minrisk_level:
            minrisk_level=risklevel
            print("found exit - risk level:",minrisk_level)
        return
    
    if cavern.shape[0]-1 > coordinates[0] and wherefrom!="E":
        nextpos(coordinates,[coordinates[0]+1,coordinates[1]],risklevel,"W")
    if cavern.shape[1]-1 > coordinates[1] and wherefrom!="S":
        nextpos(coordinates,[coordinates[0],coordinates[1]+1],risklevel,"N")

    if coordinates[0] > 0 and wherefrom!="W":
        nextpos(coordinates,[coordinates[0]-1,coordinates[1]],risklevel,"E")

    if coordinates[1] > 0 and wherefrom!="N":
        nextpos(coordinates,[coordinates[0],coordinates[1]-1],risklevel,"S")


nextpos([0,0],[0,0],-cavern[0,0],"")

print(minrisk_level)

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

minrisk_level=99999999999999999

nextpos([0,0],[0,0],-cavern[0,0],"")

print(minrisk_level)
