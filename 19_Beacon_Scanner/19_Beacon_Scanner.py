import numpy as np

#scanner0=[[0,2],[4,1],[3,3]]
#scanner1=[[-1,-1],[-5,0],[-2,1]]

def rotate4times(ar):
    i1 = [ar[0],ar[1],ar[2]]
    i2 = [ar[2],ar[1],-ar[0]]
    i3 = [-ar[0],ar[1],-ar[2]]
    i4 = [-ar[2],ar[1],ar[0]]
    return [i1,i2,i3,i4] 

def createallrotations(inp):
    arra=[]
    for ar in inp:
        te = []
        te.extend(rotate4times([ar[0],ar[1],ar[2]]))
        te.extend(rotate4times([ar[1],-ar[0],ar[2]]))
        te.extend(rotate4times([-ar[0],-ar[1],ar[2]]))
        te.extend(rotate4times([-ar[1],ar[0],ar[2]]))
        te.extend(rotate4times([ar[0],-ar[2],ar[1]]))
        te.extend(rotate4times([ar[0],ar[2],-ar[1]]))
        arra.append(te)
    return np.rot90(arra)



def find3d(beaconmap,scannermap):
    global scannerpos
    scannermap=np.array(scannermap,dtype=int)
    beaconmap=np.array(beaconmap,dtype=int)
    for i in beaconmap:
        for o in scannermap:

            difference=i-o

            tempscanner=scannermap+difference
            #print(tempscanner)
            count=0
            
            for y in tempscanner:
                if (y == beaconmap).all(axis=1).any():
                    count+=1

            if count>=12:
                #print("found solution")
                #print(i,o,difference)
                scannerpos.append(difference)

                #bm=np.array(beaconmap)
                dat=np.concatenate((beaconmap,tempscanner),axis=0)
                new_array = [tuple(row) for row in dat]
                return np.unique(new_array,axis=0),True
    return beaconmap,False






#### Convert input.txt into usable array of coordinates ####

lines=open("input.txt").readlines()
ln=0
scannermap=[]

while True:
    cl=lines[ln]
    #print(cl[0:2])
    if cl[0:3]=="---":
        #print("new Scanner info started in line:",ln)
        
        ln+=1
        beacs=[]
        while True:
            if lines[ln].strip()=="":
                break
            nums=[int(x) for x in lines[ln].strip().split(',')]
            beacs.append(nums)
            ln+=1
            if ln==len(lines):
                break
    scannermap.append(beacs)
    if ln==len(lines):
        break
    ln+=1

beaconmap=scannermap[0]
foundscanners=[0]
scannerpos=[]


#### Search for all beacons ####

for tt in range(0,5):
    for i in range(1,len(scannermap)):
        
        if i in foundscanners:
            continue
        print("Searching for scanner",i)
        te=createallrotations(scannermap[i])
        for x in te:
            beaconmap,suc=find3d(beaconmap,x)
            #print(len(beaconmap))
            if suc==True:
                print("found")
                foundscanners.append(i)
                break

print("part one:",len(beaconmap))

#### Part Two: calculate maximum manhatten distance ####
biggestdistance=0

for i in range(0,len(scannerpos)):
    t=scannerpos[i]
    for x in range(0,len(scannerpos)):
        if i==x:
            continue
        z=scannerpos[x]
        #print(z)
        distance=abs(t[0]-z[0])+abs(t[1]-z[1])+abs(t[2]-z[2])
        #print(distance)
        if distance>biggestdistance:
            biggestdistance=distance

print("part two:",biggestdistance)