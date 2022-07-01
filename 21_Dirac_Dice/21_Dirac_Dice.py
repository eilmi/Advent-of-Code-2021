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



while True:
    #player 1
    nsc,currentdicevalue=getdicenumbers(currentdicevalue,dicesides)
    currentplayerpos[0]=(currentplayerpos[0]+nsc)%10
    scorecount[0]+=currentplayerpos[0]

    # player 2
    nsc,currentdicevalue=getdicenumbers(currentdicevalue,dicesides)
    currentplayerpos[1]=(currentplayerpos[1]+nsc)%10
    scorecount[1]+=currentplayerpos[1]
    
    break