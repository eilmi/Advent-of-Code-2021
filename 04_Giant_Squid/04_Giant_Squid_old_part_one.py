import numpy as np

f = open("input.txt").readlines()
#f = open("04_Giant_Squid/input.txt").readlines()


bingo_numbers = f[0].strip().split(",")
for i in range(0, len(bingo_numbers)):
    bingo_numbers[i] = int(bingo_numbers[i])

boardends=[]
for i in range(1,len(f)):
    if f[i]=="\n":
        boardends.append(i)

boardends.append(len(f))


boards=[]
for i in range(len(boardends)-1):
    line = (f[boardends[i]+1:boardends[i+1]])
    board=[]
    for x in line:
        numbers = x.split()

        board.append(numbers)
    boards.append(board)

nparray = np.array(boards,dtype=int)


def checkifwon(numbers,boardarrays):
    for i in range(boardarrays.shape[0]): #iterate over all boards
        for x in range(boardarrays.shape[1]):
            row=boardarrays[i,x,:]
            if all(item in numbers for item in row):
                return i
        
        for x in range(boardarrays.shape[2]):
            column=boardarrays[i,:,x]
            if all(item in numbers for item in column):
                return i



for a in range(0,len(bingo_numbers)):
    nums=bingo_numbers[0:a+1]
    #print(nums)
    result = checkifwon(nums,nparray)
    if (result is not None):
        print("Board",result,"just won when",bingo_numbers[a],"was called")
        break

winningboard=np.array(nparray[result])

#print(winningboard)
tempboard=winningboard.flatten()

test = [item for item in tempboard if item not in nums]

print(sum(test)*bingo_numbers[a])

print("finished!")