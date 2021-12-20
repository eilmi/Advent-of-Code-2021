import numpy as np


lines = open("input.txt").readlines()

secondpart=False

buildinstructions=[]
foldinstructions=[]

for i in lines:
    i=i.strip()
    if (i==""):
        secondpart=True
        continue
    if secondpart:
        i=i.split()[2].split("=")
        foldinstructions.append(i)
    else:
        buildinstructions.append(i.strip().split(","))

buildinstructions=np.array(buildinstructions,dtype=int)

xmax=buildinstructions[:,0].max()+1
ymax=buildinstructions[:,1].max()+1

dotmap=np.zeros((ymax,xmax))

for i in buildinstructions:
    dotmap[i[1],i[0]]=1

firstime=True

for i in foldinstructions:
    if i[0]=="x":
        foldline=int(i[1])
        partone=dotmap[:,0:foldline]
        parttwo=dotmap[:,foldline+1:]
        dotmap=partone+np.fliplr(parttwo)

    elif i[0]=="y":
        foldline=int(i[1])
        partone=dotmap[0:foldline,:]
        parttwo=dotmap[foldline+1:,:]
        dotmap=partone+np.flipud(parttwo)

    else:
        print("ERROR - unknown fold instruction")

    if firstime:
        firstime=False
        print("Part one:",len(np.where(dotmap >=1)[1]) )


for i in range(0,8):
    x=dotmap[:,0+i*5:4+i*5]
    for t in x:
        for f in t:
            if f>=1:
                print("#",end="")
            else:
                print(".",end="")
        print("")
    print("------")