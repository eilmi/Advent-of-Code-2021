import numpy as np

f = open("input.txt").readlines()

#f[0]="3,4,3,1,2"

initstate=f[0].strip().split(",") # strip inputline to get rid off "/n" and split at ","
initstate=np.array(initstate,dtype=int) # convert array into int numpy array

def howmanyfish(begin,days):
    howmany=np.array([],dtype=np.uint32) # create a numpyarray with datatype uint32 to store how many fish have 0,1,2,3,...,8 days left

    for i in range(0,9): # check begin state on how many fish have how many days left 
        howmany=np.append(howmany,(begin==i).sum()) # 

    for d in range(days):
        newones=howmany[0] # store how many fish have 0 days left
        for s in range(1,len(howmany)): # iterate over every possible state of a fish (0 to 8 days) 
            howmany[s-1]=howmany[s]
        howmany[8]=newones # add babyfish
        howmany[6]+=newones # add fish that just created new fish
    return sum(howmany)

print("Part One:",howmanyfish(initstate,80))
print("Part Two:",howmanyfish(initstate,256))
