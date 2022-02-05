import numpy as np

lines = open("input.txt").readlines()

paths=[]
for li in lines:
    li=li.strip().split("-")
    paths.append(li)

paths=np.array(paths)


def findnextpossibleways(coordinates,alreadychecked,firstdouble):
    #at=alreadychecked.copy()
    alreadychecked.append(paths[coordinates[0],coordinates[1]])
    #print(alreadychecked)
    yarg = 1 if coordinates[1]==0 else 0
    newcarves=np.argwhere(paths==paths[coordinates[0],yarg])

    for carve in newcarves:
        carvename=paths[carve[0],carve[1]]        

        if carvename=="end":
            #print("Exit found")
            alreadychecked.append("end")
            allpossiblepaths.append(alreadychecked)
            break

        elif carvename.islower() and carvename in alreadychecked:
            if firstdouble==True and (carvename!="start"):
                findnextpossibleways(carve,alreadychecked.copy(),False)
 
        else:
            findnextpossibleways(carve,alreadychecked.copy(),firstdouble)
    return



startpoints=np.argwhere(paths=="start")

#### Part one #########
allpossiblepaths=[]
for points in startpoints:
    findnextpossibleways(points,[],firstdouble=False)

print("Part one:",len(allpossiblepaths))


##### Part two #########
allpossiblepaths=[]

for points in startpoints:
    findnextpossibleways(points,[],firstdouble=True)

print("Part two:",len(allpossiblepaths))