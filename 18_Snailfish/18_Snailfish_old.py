from typing import overload
import numpy as np
import copy


s = '[[1,2],3]'
s = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
#s = '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'

def stringtoarray(stri):
    #print(stri)
    outputarray=[]
    index = 1
    while True:

        if stri[index]=='[':
            val, i = stringtoarray(stri[index:])
            outputarray.append(val)
            index+=i
        elif stri[index]==']':
            #index+=1
            return outputarray ,index+1
        elif stri[index]==',':
            index+=1
        else:
            outputarray.append(int(stri[index]))
            index+=1
            



def modifyarray(array,listofindex,value,add):
    if add:
        if len(listofindex)==0:
            return array
        if len(listofindex)==1:
            array[listofindex]+=value
            return array
        if len(listofindex)==2:
            array[listofindex[0]][listofindex[1]]+=value
            return array
        if len(listofindex)==3:
            array[listofindex[0]][listofindex[1]][listofindex[2]]+=value
            return array
        if len(listofindex)==4:
            print(value)
            array[listofindex[0]][listofindex[1]][listofindex[2]][listofindex[3]]+=value
            return array
    else:
        if len(listofindex)==0:
            return array
        if len(listofindex)==1:
            array[listofindex]=value
            return array
        if len(listofindex)==2:
            array[listofindex[0]][listofindex[1]]=value
            return array
        if len(listofindex)==3:
            array[listofindex[0]][listofindex[1]][listofindex[2]]=value
            return array
        if len(listofindex)==4:
            array[listofindex[0]][listofindex[1]][listofindex[2]][listofindex[3]]=value
            return array        
    return False





def explode(array,depth,lastpos):
    global lastliteral
    global modifynextliteral
    global nextiteralvalue
    global farray
    ll=None
    #lastliteral=[]
    for i in range(len(array)):
        val=array[i]
        #print(val)
        if np.shape(np.array(val,dtype=object))==(): #literal value
            
            lastliteral=lastpos.copy()
            lastliteral.append(i)
            if modifynextliteral==True:
                modifynextliteral=False
                farray = modifyarray(farray,lastliteral,nextiteralvalue,True)
                return False

            continue
        else: # again a pair
            if depth==3: # explode!!
                #print("Explode")
                print("Pair to explode:",val," ---- Last literal:",lastliteral)
                farray=modifyarray(farray,lastliteral,val[0],True)
                print(lastpos+[i])
                farray=modifyarray(farray,lastpos+[i],0,False)
                nextiteralvalue=val[1]
                modifynextliteral=True

            else:
                #print(lastliteral)
                if explode(val,depth+1,lastpos+[i])==False:
                    return False

    if ll!=None:
        lastliteral.append(ll)
    return array, lastliteral


def split(array,lastpos):
    global farray
    for i in range(len(array)):
        val=array[i]
        #print(val)
        if np.shape(np.array(val,dtype=object))==(): #literal value

            if val>9:
                if val%2==0:
                    te=[int(val/2),int(val/2)]
                else:
                    te=[int(val/2),int(val/2+1)]
                farray=modifyarray(farray,lastpos+[i],te,False)
                return False
        else:
            if split(val,lastpos+[i]):
                return False
        




farray = stringtoarray(s)[0]

#print(array)

lastliteral=[]
modifynextliteral = False

#lines = open("input.txt").readlines()
lines = open("demo.txt").readlines()

farray=stringtoarray(lines[0].strip())[0]

for i in lines[1:]:
    farray=[farray,stringtoarray(i.strip())[0]]
    lastliteral=[]
    modifynextliteral = False
    while True:
        oldarray=copy.deepcopy(farray)
        #print(oldarray)
        explode(farray,0,[])
        split(farray,[])
        #print(farray)
        #print(oldarray)
        if farray==oldarray:
            break

            

print(farray)