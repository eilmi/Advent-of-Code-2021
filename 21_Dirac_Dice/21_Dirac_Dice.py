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


playerwins=[0,0]
createduniverses=0

def createnewuniverse(playerscore,playerpos,dicevalues):
    global playerwins
    global createduniverses
    while True:
        for x in range(0,6):
            if dicevalues[x]==0:
                newdicevalues=dicevalues.copy()
                for i in range(1,4):
                    newdicevalues[x]=i
                    createduniverses+=1
                    #print(newdicevalues)
                    createnewuniverse(playerscore,playerpos,newdicevalues)
        #print(dicevalues)
        dicesum=sum(dicevalues[0:3])
        playerpos[0]=((playerpos[0]+dicesum)-1)%10+1
        playerscore[0]+=playerpos[0]
        #print(dicesum)
        if playerscore[0]>=21:
            playerwins[0]+=1
            return


        # for x in range(3,6):
        #     if dicevalues[x]==0:
        #         newdicevalues=dicevalues.copy()
        #         for i in range(1,4):
        #             newdicevalues[x]=i
                    
        #             #print(newdicevalues)
        #             createnewuniverse(playerscore,playerpos,newdicevalues)
        #         return
        #print(dicevalues)
        dicesum=sum(dicevalues[3:6])
        playerpos[1]=((playerpos[1]+dicesum)-1)%10+1
        playerscore[1]+=playerpos[1]
        #print(dicesum)
        if playerscore[1]>=21:
            playerwins[1]+=1
            return

        
        createnewuniverse(playerscore.copy(),playerpos.copy(),[0,0,0,0,0,0])
    return

rr=[]

createnewuniverse([0,0],[4,8],[0,0,0,0,0,0])

print(playerwins[1])
print(createduniverses)