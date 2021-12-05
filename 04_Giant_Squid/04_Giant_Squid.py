import numpy as np

f = open("input.txt").readlines()
#f = open("04_Giant_Squid/input.txt").readlines()


bingo_numbers = f[0].strip().split(",")# extract the numbers from the first line of the file


for i in range(0, len(bingo_numbers)): #convert the string array into an int array
    bingo_numbers[i] = int(bingo_numbers[i])

#find all empty lines  and therefor the start and endings of all given boards
boardends=[]
for i in range(1,len(f)): # iterate over all lines of the file excluding the first one
    if f[i]=="\n": #check if line of file is empty
        boardends.append(i) # if so add current line index to boardends array

boardends.append(len(f)) # add last boardend manually because the file doesnt end with a empty line


#create an 3-dimensional array containing all boards
boards=[]
for i in range(len(boardends)-1): 
    block = (f[boardends[i]+1:boardends[i+1]])
    board=[]
    for x in block:
        numbers = x.split() # split line of file into array of numbers for example: ["12 42 7"] -> [12,42,7]

        board.append(numbers) #append this array of numbers to current board array 
    boards.append(board) # append this board to the array of boards

nparray = np.array(boards,dtype=int)


def checkifwon(numbers,boardarrays,wonboards=[]):
    _won_boards=wonboards
    for i in range(boardarrays.shape[0]): #iterate over all boards
        if i in _won_boards: # if board with i as index has already won skip checking and move on to next one
            continue
        for x in range(boardarrays.shape[1]): #check if a row of a board has won
            row=boardarrays[i,x,:] # get row of board
            if all(item in numbers for item in row):
                _won_boards.append(i) #add index of this board to the won_board array
        
        for x in range(boardarrays.shape[2]): #check if a column of a board has won
            column=boardarrays[i,:,x] # get column of board
            if all(item in numbers for item in column): # check if all numbers of this column are in the list of already drawn numbers
                _won_boards.append(i) # add index of this board to the won_board array

    return list(dict.fromkeys(_won_boards)) # remove duplicates from array and return it 


a_list=list(range(0,len(boards)))
firstwinner=True
result=[]

for a in range(0,len(bingo_numbers)):
    nums=bingo_numbers[0:a+1] # array of already drawn numbers
    #print(nums)
    result = checkifwon(nums,nparray,result) # check which boards win with these drawn numbers
    yet_to_win_boards = [item for item in a_list if item not in result]
    #print(bingo_numbers[a],yet_to_win_boards)


    if (len(result)==1 and firstwinner==True):
        firstwinner=False
        winnernumber=a
        winnerboard=result[0]
        print("Board",winnerboard,"just won when",bingo_numbers[a],"was called")

    if (len(yet_to_win_boards)==1):
        loserindex=yet_to_win_boards[0]

    if (len(yet_to_win_boards)==0):
        print(bingo_numbers[a],"called - last winning board is Nr.", loserindex)
        losernumber=a
        break

winningboard=np.array(nparray[winnerboard])
losingboard=np.array(nparray[loserindex])

#print(winningboard)
tempboard=winningboard.flatten()


notmarkednumbers = [item for item in tempboard if item not in bingo_numbers[0:winnernumber+1]]


print(sum(notmarkednumbers)*bingo_numbers[winnernumber])


tempboard=losingboard.flatten()


notmarkednumbers = [item for item in tempboard if item not in bingo_numbers[0:losernumber+1]]


print(sum(notmarkednumbers)*bingo_numbers[losernumber])

print("finished!")