import numpy as np

f = open("input.txt").readlines()

#f[0]="3,4,3,1,2"

state=f[0].strip().split(",")


for i in range(0, len(state)): #convert the string array into an int array
    state[i] = int(state[i])
state2=np.array(state)

for i in range(80):
    newones=0
    for fish in range(len(state)):
        if state[fish]==0:
            state[fish]=6
            newones+=1
        else:
            state[fish]-=1
    for babyfish in range(newones):
        state.append(8)

print(len(state))