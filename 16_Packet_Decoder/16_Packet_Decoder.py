import numpy as np

def decode_packet(s,nrofpackets):
    global totalversionsum
    literalarray=[]
    currentpacket=1
    lastindex=0
    while True:
        content=s[lastindex:]

        packetversion=int(content[0:3],2)
        totalversionsum+=packetversion

        typeid=int(content[3:6],2)
        print("Packet version:",packetversion,"type id:",typeid,end="")

        #content=s[6:] 

        if typeid==4: # literal value
            print(" -> Literal Packet",end="")
            #print(content)

            i=0
            binnumber=''
            while True:
                t=content[6+i*5:11+i*5]
                #print(t)
                binnumber+=t[1:]
                if t[0]=="0":
                    break
                i+=1
            print(" with value:",int(binnumber,2),"decoded")
            literalarray.append(int(binnumber,2))
            lastindex+=11+i*5



        else: # operator packet
            print(" -> operator packet",end="")
            length_type_id=int(content[6],2)
            if length_type_id==0: # next 15 bits are number of bits
                print(" - Length type id:",0,end="")
                length=int(content[7:22],2)
                print(" -> Number of bits:",length)
                value, li = decode_packet(content[22:22+length],-1)
                #literalarray.append(value)
                lastindex+=22+length
            else: # next 11 bits are number of sub packets
                length=int(content[7:18],2)
                print(" -> Number of subpackets:",length)
                value,li = decode_packet(content[18:],length)
                #literalarray.append(value)
                lastindex+=18+li

            if typeid==0:
                literalarray.append(sum(value))
            elif typeid==1:
                literalarray.append(np.prod(value,dtype=np.int64))
            elif typeid==2:
                literalarray.append(min(value))
            elif typeid==3:
                literalarray.append(max(value))
            elif typeid==5:
                if len(value)!=2:
                    print("ERROR")
                literalarray.append(1 if value[0]>value[1] else 0)
            elif typeid==6:
                if len(value)!=2:
                    print("ERROR")
                literalarray.append(1 if value[0]<value[1] else 0)
            elif typeid==7:
                if len(value)!=2:
                    print("ERROR")
                literalarray.append(1 if value[0]==value[1] else 0)
            else:
                print("ERROR")
                    
        if nrofpackets==-1:
            if len(s)-lastindex>0:
                continue
            else:
                break
        else:
            if currentpacket==nrofpackets:
                break
            else:
                currentpacket+=1

    print(literalarray)
    return literalarray,lastindex

        

f = open("input.txt").readlines()

f=f[0].strip()
#f = "D2FE28"
#f = "38006F45291200"
#f = "9C0141080250320F1802104A08"

r = "{0:08b}".format(int(f, 16)).zfill(4*len(f))
print(r)
totalversionsum=0


values, li = decode_packet(r,1)

print("Part one:",totalversionsum)
print("Part Two:",values[0])


#501 is too low

# 241930482683 too low for part 2
# 241937017731 is too low