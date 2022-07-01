from functools import reduce
import numpy as np

lines=open("input.txt").readlines()

iea=[]
for i in lines[0]:
    if i=='#':
        iea.append(1)
    elif i=='.':
        iea.append(0)
    else:
        pass

img=[]
for i in lines[2:]:
    l=[]
    for x in i:
        if x=='#':
            l.append(1)
        elif x=='.':
            l.append(0)
        else:
            pass
    img.append(l)


def convertmaptopixel(surrpixels,algorithm):
    #st=''.join(surrpixels[0])+''.join(surrpixels[1])+''.join(surrpixels[2])
    #st=str.replace(st,'.','0').replace('#','1')
    ind=int(reduce(lambda a,b: 2*a+b, surrpixels.reshape(-1)))
    #print(st)
    #ind=(int(st,2))
    #print(ind)
    return algorithm[ind]

def getsurrpixels(map,coords,default):
    maxy=len(map)
    maxx=len(map[0])
    surrpixels=np.empty(shape=(3,3),dtype=np.int)
    for dy in range(0,3):
        for dx in range(0,3):
            surrpixels[dy][dx]=map[coords[0]-1+dy][coords[1]-1+dx] if (coords[0]-1+dy>=0 and coords[1]-1+dx>=0 and coords[0]-1+dy<maxy and coords[1]-1+dx<maxx) else default

    return surrpixels

def getlitpixelcount(image,iterations):
    default=0
    img=image.copy()
    for tt in range(iterations):
        newimg=[]
        for y in range(-1,len(img)+1):
            row=[]
            for x in range(-1,len(img[0])+1):
                row.append(convertmaptopixel(getsurrpixels(img,[y,x],default),iea))
            newimg.append(row)
        img=newimg.copy()
        default=convertmaptopixel(getsurrpixels(img,[-2,-2],default),iea)
    return np.sum(img)

print("part one:")
print(getlitpixelcount(img,2))
print("part two:")
print(getlitpixelcount(img,50))