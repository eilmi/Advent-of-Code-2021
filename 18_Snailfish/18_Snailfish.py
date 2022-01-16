import math

def seperateexploding(stri,i,lastliteral):
    pa=stri[i+1:]
    ende=i+pa.index(']')+2
    #print(i,ende)
    er=pa.partition("]")[0]
    er = er.split(',')
    #print(pa)
    firstvalue=int(er[0])
    secondvalue=int(er[1])

    if lastliteral!=None:
        #stri[lastliteral]=str(int(stri[lastliteral])+firstvalue)
        if lastliteral!=len(stri) and stri[lastliteral+1].isdigit():
            endindex=lastliteral+2
        else:
            endindex=lastliteral+1
        value=int(stri[lastliteral:endindex])

        newvalue=value+firstvalue

        stri=stri[:lastliteral]+str(newvalue)+stri[endindex:]

        if newvalue>=10 and value<10:
            i+=1
            ende+=1

        #print(value)

    #print(stri)
    stri=stri[:i]+"0"+stri[ende:]

    di=ende-i-1
    
    lastpart=stri[ende-di:]

    #print(lastpart)

    for i in range(len(lastpart)):
        digit = lastpart[i]
        if digit.isdigit():
            st=ende-di+i
            en=st+1
            if lastpart[i+1].isdigit():
                en+=1

            #print(st,en)
            value=int(stri[st:en])
            newvalue=value+secondvalue
            stri=stri[:st]+str(newvalue)+stri[en:]
            break

    return stri



def explode(stri):
    depth=0
    lastliteralpos=None
    for i in range(len(stri)):
        ch=stri[i]
        if ch == '[':
            depth+=1
            if depth==5:
                return seperateexploding(stri,i,lastliteralpos)
        elif ch ==']':
            depth-=1
        elif ch.isdigit():
            if lastliteralpos==None or i-lastliteralpos>1:
                lastliteralpos=i

    return stri

def split(stri):
    for i in range(len(stri)):
        if stri[i].isdigit() and stri[i+1].isdigit():
            value=int(stri[i:i+2])
            #print(value)
            ins='['+str(int(value/2))+','+str(math.ceil(value/2))+']'
            stri=stri[:i]+ins+stri[i+2:]
            break

    return stri


def addition(stri1,stri2):
    return '['+stri1+','+stri2+']'


def calcsum(stri,lastindex):
    val=0
    i=lastindex
    while True:
        ch=stri[i]
        if ch=='[':
            firstval,i=calcsum(stri,i+1)
        if ch==',':
            secondval,i=calcsum(stri,i+1)
        if ch==']':
            return int(firstval)*3+int(secondval)*2,i
        elif ch.isdigit():
            return int(ch),i
        i+=1
            

def reduce(stri):
    while True:
        news = explode(stri)
        if str(news) != str(stri):
            stri=str(news)
            #print(s)
            continue

        news = split(stri)
        if str(news) != str(stri):
            stri=str(news)
            continue

        #print("=",s)
        break
    return stri


lines=open("input.txt").readlines()
s=lines[0].strip()

for i in lines[1:]:
    #print(" ",s)
    #print("+",i.strip())
    s=addition(s,i.strip())
    s=reduce(s)


print("part one:",calcsum(s,0)[0])

maxsumme=0

for i in range(len(lines)):
    line1=lines[i]
    for x in range(len(lines)):
        if i==x:
            continue
        line2=lines[x]
        s=addition(line1,line2)
        s=reduce(s)
        summe=calcsum(s,0)[0]
        if summe>maxsumme:
            maxsumme=summe

print("part two",maxsumme)


