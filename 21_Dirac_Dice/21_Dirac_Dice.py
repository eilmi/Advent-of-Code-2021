lines=open("input.txt").readlines()

initialplayerpos=[]

for i in lines: #read starting position of both players from puzzle input
    initialplayerpos.append(int((i.strip().split(':')[1])))

scorecount=[0,0]
currentdicevalue=1
dicesides=100
currentplayerpos=initialplayerpos.copy()

def getdicenumbers(val,max):
    """
    Rolls the dice 3 times in a row and returns sum of all 3 and last dice result
    increases diced value by 1 with each roll unless param max is reached in which case it resets to 1

    :param val: value of first dice roll
    :param max: maximum value which the dice can reach
    :return: sum of the three dice rolls, last dice value
    """
    f=0
    for i in range(3):
        f+=val
        if val<max:
            val+=1
        else:
            val=1
    return f,val


print("part one:")
t=0
while True:
    #player 1
    nsc,currentdicevalue=getdicenumbers(currentdicevalue,dicesides)
    currentplayerpos[0]=((currentplayerpos[0]+nsc)-1)%10+1
    scorecount[0]+=currentplayerpos[0]
    t+=3
    if scorecount[0]>=1000:
        print("Player 1 won: "+str(scorecount[1]*t))
        break

    # player 2
    nsc,currentdicevalue=getdicenumbers(currentdicevalue,dicesides)
    currentplayerpos[1]=((currentplayerpos[1]+nsc)-1)%10+1
    scorecount[1]+=currentplayerpos[1]
    t+=3
    if scorecount[1]>=1000:
        print("Player 2 won: "+str(scorecount[0]*t))
        break

###################### Part two ##########################
totalposs=[0,0] # list that stores how many ways have already been found in which either player 1 or player 2 win the game
dicevalues=[3,4,5,6,7,8,9] # list of possible results when the dice is rolled three times
possibleways=[1,3,6,7,6,3,1] # list of how many different ways there are to archive the specific dice result

def newuniverses(positions,scores,possibilities):
    """


    :param positions: 
    :param scores:
    :param possibilities:
    :return:
    """
    
    if scores[0]>=21: #check if player 1 has already a score of 21 or more
        totalposs[0]+=possibilities # add number of possibilities that lead to this result to total count of ways in which player 1 wins the game
        return True # return True to prevent counting this way to the victory multiple times (when player 1 wins the game, player 2 doesn't create new universes anymore in which player 1 would win again)

    if scores[1]>=21: # check if player 2 has a score of 21 or more
        totalposs[1]+=possibilities # add number of possibilities that lead to this result to total count of ways in which player 2 wins the game
        return False # return False so that player 2 can create all of it's possible universes

    newposition=[0,0]
    newscore=[0,0]
    for i in range(0,7): # iterate over all possible dice values for player 1 (3 to 9)
        newposition[0]=((positions[0]+dicevalues[i])-1)%10+1 # calculate new position of player 1 on the game board (somewhere between 1 and 10)
        newscore[0]=scores[0]+newposition[0] # calculate new score of player 1

        for x in range(0,7): # iterate over all possible dice values for player 2 (3 to 9)
            newposition[1]=((positions[1]+dicevalues[x])-1)%10+1 # calculate new position of player 2 on the game board (somewhere between 1 and 10)
            newscore[1]=scores[1]+newposition[1] # calculate new score of player 2
            
            if newuniverses(newposition,newscore,possibilities*possibleways[i]*possibleways[x]): # create new universe with new player positions and scores
                break # break out of the loop in which player 2 creates all of it's possible universes because player 1 has already won


newuniverses(initialplayerpos,[0,0],1)

print("part two:")
if totalposs[0]>totalposs[1]:
    print("Player 1 won in more universes:",totalposs[0])
else:
    print("Player 2 won in more universes:",totalposs[1])