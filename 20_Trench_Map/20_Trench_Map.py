lines=open("input.txt").readlines()

iea=lines[0]
img=[]
for i in lines[2:]:
    img.append(i.strip())


def getx(x,ar):
    if x<-1:
        return '...'
    if x==-1:
        return '..'+ar[0]

    elif x==0:
        return '.'+ar[0:2]
        
    elif x==len(ar)-1:
       
        return ar[x-1:x+1]+'.'

    elif x==len(ar):
        return ar[x-1]+'..'
    #elif x-1==len(ar):
        #print("ERROR")
    elif x>len(ar):
        return '...'
    else:
        return ar[x-1:x+2]



for tt in range(2):
    newimg=[]
    for i in range(-4,len(img)+4):
        teimg=''
        for x in range(-4,len(img[0])+4):
            
            temp=[]
            if (i==-1):
                temp.append('...')
                temp.append('...')
                temp.append(getx(x,img[0]))
            elif i==0:
                temp.append('...')
                temp.append(getx(x,img[i]))
                temp.append(getx(x,img[i+1]))
                
            elif i>0 and i<len(img)-1:
                temp.append(getx(x,img[i-1]))
                temp.append(getx(x,img[i]))
                temp.append(getx(x,img[i+1]))
            elif i==len(img)-1:
                temp.append(getx(x,img[i-1]))
                temp.append(getx(x,img[i]))
                temp.append('...')
            elif i==len(img):
                temp.append(getx(x,img[i-1]))
                temp.append('...')
                temp.append('...')
            else:
                temp.append('...')
                temp.append('...')
                temp.append('...')

            print(temp,end="")
            st=temp[0]+temp[1]+temp[2]
            st=str.replace(st,'.','0').replace('#','1')
            ind=(int(st,2))
            teimg+=iea[ind]
        newimg.append(teimg)
        print("")
    print(img)
    img=newimg.copy()

print(img)
pixelcount=0
for i in img:
    for t in i:
        if t=='#':
            pixelcount+=1

print(pixelcount)


# 5504 is too high

#5201 is too low