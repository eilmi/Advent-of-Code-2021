input = "target area: x=153..199, y=-114..-75"
#input = "target area: x=20..30, y=-10..-5"

input=input.split()

input=input[2:]

xin=input[0][2:-1].split("..")
yin=input[1][2:].split("..")


ymax=abs(int(yin[0]))-1
ymin=int(yin[0])
xmax=int(xin[1])

def calcsum(x):
    t=0
    for i in range(0,x+1):
        t+=i
    return t
print ("part one:",calcsum(ymax))

xmin=0
while True:
    if calcsum(xmin)<int(xin[0]):
        xmin+=1
    else:
        break

#print(xmin)


#################### Part Two #########################

def calcnewposandvel(vel,pos):
    pos[0]+=vel[0]
    pos[1]+=vel[1]
    vel[1]-=1
    if vel[0]>0:
        vel[0]-=1
    elif vel[0]<0:
        vel[0]+=1

    return vel,pos

vel=[6,9]
pos=[0,0]

counter=0
for x in range(xmin,xmax+1):
    for y in range(ymin,ymax+1):
        pos=[0,0]
        vel=[x,y]
        while True:
            if pos[0]>int(xin[1]) or pos[1]<int(yin[0]):
                break
            if (pos[0]<=int(xin[1]) and pos[0]>=int(xin[0])) and pos[1]>=int(yin[0]) and pos[1]<=int(yin[1]):
                counter+=1
                break
            vel,pos=calcnewposandvel(vel,pos)

print("part two:",counter)

