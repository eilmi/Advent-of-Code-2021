import numpy as np

lines=open("input.txt").readlines()

instructions=[]
for i in lines:
    ins=[]
    t = i.strip().split(" ")
    #print(t)
    ins.append(t[0])
    coords=t[1].split(",")
    #print(coords)
    xcoords=[int (i) for i in coords[0].replace("x=",'').split("..")]
    ycoords=[int (i) for i in coords[1].replace("y=",'').split("..")]
    zcoords=[int (i) for i in coords[2].replace("z=",'').split("..")]

    ins.append(xcoords)
    ins.append(ycoords)
    ins.append(zcoords)
    instructions.append(ins)


instructions=np.array(instructions,dtype=object)

minx=min(instructions[:,1])[0]
maxx=max(instructions[:,1])[1]

miny=min(instructions[:,2])[0]
maxy=max(instructions[:,2])[1]

minz=min(instructions[:,3])[0]
maxz=max(instructions[:,3])[1]

print(minz)

sizex=maxx-minx
sizey=maxy-miny
sizez=maxz-minz

turnedoncubes=[]

for x in range(-50,51,1):
    for y in range(-50,51,1):
        for z in range(-50,51,1):
            
            pass

print("END")