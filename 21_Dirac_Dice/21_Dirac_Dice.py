lines=open("demo.txt").readlines()

currentplayerpos=[]
scorecount=[0,0]

for i in lines:
    currentplayerpos.append(int((i.strip().split(':')[1])))

currentdicevalue=1
dicesides=100

def getdicenumbers(val,max):
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

## Part Two
totalposs=[0,0]


def newuniverses(positions,scores,possibilities):
    _poss=possibilities
    #global totalposs
    dicevalues=[3,4,5,6,7,8,9]
    possibleways=[1,3,6,7,6,3,1]


    if scores[0]>=21:
        if scores[1]<21:
            totalposs[0]+=possibilities
            #next
        return
        #print(possibilities)
        #totalposs[0]+=possibilities
        #print(totalposs)
        return

    if scores[1]>=21:
        #print(possibilities)
        totalposs[1]+=possibilities
        #print(totalposs)
        return

    
    newposition=[0,0]
    newscore=[0,0]
    for i in range(0,7):
        newposition[0]=((positions[0]+dicevalues[i])-1)%10+1
        newscore[0]=scores[0]+newposition[0]
        for x in range(0,7):

            newposition[1]=((positions[1]+dicevalues[x])-1)%10+1
            newscore[1]=scores[1]+newposition[1]
            
            newuniverses(newposition,newscore,possibilities*(possibleways[i]*possibleways[x]))


newuniverses([4,8],[0,0],1)

print(totalposs)