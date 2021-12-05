f = open("instructions.txt").readlines()

print("Part one:")

hor = 0
depth = 0

for i in f:
    t = i.split()
    #print(t)
    if t[0]=="up":
        depth-=int(t[1])
    elif t[0]=="forward":
        hor+=int(t[1])
    elif t[0]=="down":
        depth+=int(t[1])
    else:
        print("ERROR!")


print(hor*depth)

# Part Two
print("Part two:")

hor =0
depth=0
aim=0
for i in f:
    t = i.split()
    #print(t)
    if t[0]=="up":
        aim-=int(t[1])
    elif t[0]=="down":
        aim+=int(t[1])
    elif t[0]=="forward":
        hor+=int(t[1])
        depth+=aim*int(t[1])

    else:
        print("ERROR!")


print(hor*depth)