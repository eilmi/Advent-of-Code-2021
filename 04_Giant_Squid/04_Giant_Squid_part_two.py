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
    won_boards=[]
    for i in range(boardarrays.shape[0]): #iterate over all boards

        for x in range(boardarrays.shape[1]):
            row=boardarrays[i,x,:]
            if all(item in numbers for item in row):
                won_boards.append(i)
        
        for x in range(boardarrays.shape[2]):
            column=boardarrays[i,:,x]
            if all(item in numbers for item in column):
                won_boards.append(i)

    return won_boards


a_list=list(range(0,len(boards)))
firstwinner=True

for a in range(0,len(bingo_numbers)):
    nums=bingo_numbers[0:a+1]
    #print(nums)
    result = checkifwon(nums,nparray)
    yet_to_win_boards = [item for item in a_list if item not in list(dict.fromkeys(result))]
    #print(bingo_numbers[a],yet_to_win_boards)


    if (len(result)==1 and firstwinner==True):
        firstwinner=False
        winnernumber=a
        winnerindex=result[0]
        print("Board",winnerindex,"just won when",bingo_numbers[a],"was called")

    if (len(yet_to_win_boards)==1):
        loserindex=yet_to_win_boards[0]

    if (len(yet_to_win_boards)==0):
        print(bingo_numbers[a],"called - last winning board is Nr.", loserindex)
        losernumber=a
        break

winningboard=np.array(nparray[winnerindex])
losingboard=np.array(nparray[loserindex])

#print(winningboard)
tempboard=winningboard.flatten()


notmarkednumbers = [item for item in tempboard if item not in bingo_numbers[0:winnernumber+1]]


print(sum(notmarkednumbers)*bingo_numbers[winnernumber])


tempboard=losingboard.flatten()


notmarkednumbers = [item for item in tempboard if item not in bingo_numbers[0:losernumber+1]]


print(sum(notmarkednumbers)*bingo_numbers[losernumber])

print("finished!")