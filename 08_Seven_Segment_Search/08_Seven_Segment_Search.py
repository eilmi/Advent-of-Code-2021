import numpy as np

f = open("input.txt").readlines()

# ------------   Part one  --------------------
numbers=0

for i in f: # run for all lines in file
    i=i.strip().split(" | ") # strip away /n and split string at " | "
    rs=i[1].split() # split second array element at all whitespaces and store it
    for c in rs: # run for all elements in array
        if len(c)==2 or len(c)==3 or len(c)==4 or len(c)==7: # check if current array elements has specific length
            numbers+=1 # if so add 1 to 'numbers'

print("Part one:",numbers)



# ------------- Part two ---------------------
def getnumber(ls,rs):
    st=""

    # get elements ('a','b',...'g') of numbers with unique length and stores them in list

    seven=set([word for word in ls if len(word) == 3][0]) # only "7" is made out of 3 elements in 7-segment-display
    four=set([word for word in ls if len(word) == 4][0]) # "4" is made out of 4 elements
    eight=set([word for word in ls if len(word) == 7][0]) # "8" needs all 7 elements

    temp =set(rs) # parse string into list of unique characters f.e.:  set("acf") = {"a","c","f"} 

    if (len(temp)==6):
        if(all(s in temp for s in four)) and (all(s in temp for s in seven)):
            st="9"
        elif(all(s in temp for s in seven)) and not (all(s in temp for s in four)):
            st="0"
        else:
            st="6"
    elif (len(temp)==2):
        st="1"
    elif(len(temp)==3):
        st="7"
    elif(len(temp)==4):
        st="4"
    elif(len(temp)==7):
        st="8"
    elif (len(temp)==5):
        if (all(s in temp for s in seven)):
            st="3"
        else:
            combined = set("".join(temp).join(four)) # combine current instruction with that of number 4
            #print(test,eight)
            if all(s in combined for s in eight): # check if combination includes all elements (number 8)
                st="2"
            else:
                st="5"
    else:
        print("Error")
    
    return(st)



numbers=[]

for  i in f:
    num=''
    i=i.strip().split(" | ")
    rs=i[1].split()
    ls=i[0].split()
    #print(ls)
    for i in range(len(rs)):
        num+=getnumber(ls,rs[i])
    numbers.append(int(num))
    #print(num)

print("Part two:",sum(numbers))