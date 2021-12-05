import numpy as np


#f = open("input.txt").readlines()
f = open("03_Binary_Diagnostic/input.txt").readlines()


arr =[]


def findmajmin(test):
    gamma=""
    epsilon=""

    for i in range(test.shape[1]):
        summe=sum(test[:,i])
        if (summe)>=(test.shape[0]/2):
            gamma+="1"
            epsilon+="0"
        else:
            gamma+="0"
            epsilon+="1"
    return [gamma,epsilon]





for lines in f:
    li = []
    lines=lines.strip()
    for chars in lines:
        li.extend(chars)
    arr.append(li)

nparray = np.array(arr,dtype=int)


gamma,epsilon=findmajmin(nparray)

print(int(gamma,2)*int(epsilon,2))


#part two

oxygenarray=np.array(arr,dtype=int)
c02array=np.array(arr,dtype=int)


print("part two:")
for i in range(nparray.shape[1]):
    #print(oxygenarray)
    gamma,epsilon=findmajmin(oxygenarray)
    dellines=[]
    #print(gamma)
    #print(int(gamma[i]))
    for x in range(oxygenarray.shape[0]):
        if oxygenarray[x,i]!=int(gamma[i]):
            dellines.append(x)   
    oxygenarray=np.delete(oxygenarray,dellines,0)
    #print(dellines)
    if(len(oxygenarray)==1):
        break   

for i in range(nparray.shape[1]):
    #print(c02array)
    gamma,epsilon=findmajmin(c02array)
    dellines=[]
    #print(gamma)
    #print(int(gamma[i]))
    for x in range(c02array.shape[0]):
        if c02array[x,i]!=int(epsilon[i]):
            dellines.append(x)   
    c02array=np.delete(c02array,dellines,0)
    #print(dellines)
    if(len(c02array)==1):
        break   

oxy=''.join(str(x) for x in oxygenarray[0])
co2=''.join(str(x) for x in c02array[0])

print(int(oxy,2)*int(co2,2))