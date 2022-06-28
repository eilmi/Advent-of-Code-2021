import numpy as np

lines=open("input.txt").readlines()

iea=lines[0]
img=[]
for i in lines[2:]:
    img.append(i.strip())


def convertmaptopixel(surrpixels,algorithm):
    st=''.join(surrpixels[0])+''.join(surrpixels[1])+''.join(surrpixels[2])
    st=str.replace(st,'.','0').replace('#','1')
    #print(st)
    ind=(int(st,2))
    #print(ind)
    return algorithm[ind]

def getsurrpixels(map,coords,default):
    maxy=len(map)
    maxx=len(map[0])
    surrpixels=np.empty(shape=(3,3),dtype=np.str)
    for dy in range(0,3):
        for dx in range(0,3):
            surrpixels[dy][dx]=map[coords[0]-1+dy][coords[1]-1+dx] if (coords[0]-1+dy>=0 and coords[1]-1+dx>=0 and coords[0]-1+dy<maxy and coords[1]-1+dx<maxx) else default
    #surrpixels[0][0]=map[coords[0]-1][coords[1]-1] if (coords[0]-1>=0 and coords[1]-1>=0 and coords[0]-1<maxy and coords[1]-1<maxx) else default
    #surrpixels[0][1]=map[coords[0]-1][coords[1]] if (coords[0]-1>=0 and coords[1]>=0 and coords[0]-1<maxy and coords[1]<maxx) else default
    #surrpixels[0][2]=map[coords[0]-1][coords[1]+1] if (coords[0]-1>=0 and coords[1]+1>=0 and coords[0]-1<maxy and coords[1]+1<maxx) else default

    return surrpixels


default='.'
for tt in range(50):
    newimg=[]
    for y in range(-1,len(img)+1):
        row=''
        for x in range(-1,len(img[0])+1):
            row+=convertmaptopixel(getsurrpixels(img,[y,x],default),iea)
        newimg.append(row)
    img=newimg.copy()
    default=convertmaptopixel(getsurrpixels(img,[-2,-2],default),iea)

pixelcount=0
for i in img:
    for t in i:
        if t=='#':
            pixelcount+=1

print(pixelcount)

# 5504 is too high

#5201 is too low