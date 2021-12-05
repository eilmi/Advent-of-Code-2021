import numpy as np

f = open("input.txt").readlines() # open file and store all lines in an array

def findmajmin(test):
    gamma="" # gamma mask
    epsilon="" # epsilon mask

    for i in range(test.shape[1]): # run for all columns of array
        summe=sum(test[:,i]) # get sum of current column
        if (summe)>=(test.shape[0]/2): # check if more than the half of this column is 1 instead of 0
            gamma+="1" # add 1 to gamma mask
            epsilon+="0" # add 0 to epsilon mask
        else:
            gamma+="0"
            epsilon+="1"
    return [gamma,epsilon] #return gamma and epsilon mask

#create numpy array
arr =[]

for lines in f: # run for all lines in file
    li = []
    lines=lines.strip()# get rid of /n
    for chars in lines: # run for all characters in line
        li.extend(chars) # extend li array by character
    arr.append(li) # append li array to arr array

nparray = np.array(arr,dtype=int) # convert standard python array into numpy one

# ---------- Part one --------------

gamma,epsilon=findmajmin(nparray) # get gamma and epsilon mask of array

print("Part One:",int(gamma,2)*int(epsilon,2))


# ---------- Part two --------------

def sortoutvalues(array,index):
    for i in range(array.shape[1]): # run for all columns in array
        #print(oxygenarray)
        result=findmajmin(array) # get gamma and epsilon mask of current array
        mask=result[index] # use whether gamma or epsilon mask 
        dellines=[] # array for indicies of all rows which have to be deleted

        for x in range(array.shape[0]):# run for all rows of array
            if array[x,i]!=int(mask[i]): # check if value in i-column and x-row is equal to mask
                dellines.append(x) # if not: store index of this line in array

        array=np.delete(array,dellines,0) # delete all rows in array in which the mask was different
        #print(dellines)
        if(len(array)==1): # if only one row is left return it
            return array[0]
    return

oxygenarray=sortoutvalues(nparray,0) # sort out values using gamma mask
c02array=sortoutvalues(nparray,1) # sort out values using epsilon mask

# convert the integer arrays containing 0 and 1 to strings
oxy=''.join(str(x) for x in oxygenarray)
co2=''.join(str(x) for x in c02array)

print("Part Two:",int(oxy,2)*int(co2,2)) # convert the numbers from binary to decimal and multiply it