import numpy as np

lines = open("input.txt").readlines()

def returnoppositebracket(cha):
    if cha=="]":
        return "["
    if cha==">":
        return "<"
    if cha=="}":
        return "{"
    if cha==")":
        return "("

    if cha=="[":
        return "]"
    if cha=="<":
        return ">"
    if cha=="{":
        return "}"
    if cha=="(":
        return ")"
    return False 


notcompletedmissing=[]
errorpointarray=[]
for i in lines:
    i=i.strip()
    prev=[]
    errorcount=0
    firsterror=True
    
    errorpoints=0
    for ch in i:
        if len(prev)==0:
            prev.append(ch)
            continue
        if ch in ["(","{","<","["]:
            prev.append(ch)
        else:
            if returnoppositebracket(ch) == prev[-1]:
                prev.pop()
            else:
                errorcount+=1
                if firsterror==True:
                    firsterror=False
                    if ch==")":
                        errorpoints=3
                    elif ch=="]":
                        errorpoints=57
                    elif ch=="}":
                        errorpoints=1197
                    elif ch==">":
                        errorpoints=25137
                    else:
                        print("Error")
    errorpointarray.append(errorpoints)
    if len(prev)!=0 and errorcount==0:
        notcompletedmissing.append(prev)

print("part one:",sum(errorpointarray))

####### Part two ############

points=[]

for i in notcompletedmissing:
    errorpoints=0
    for x in i[::-1]: #reverse array an iterate over all elements
        errorpoints*=5 # multiply by 5
        brak=returnoppositebracket(x)
        if brak==")":
            errorpoints+=1
        if brak=="]":
            errorpoints+=2
        if brak=="}":
            errorpoints+=3
        if brak==">":
            errorpoints+=4
    points.append(errorpoints)

print("part two:",int(np.median(points)))
