
f = open("input.txt").readlines()

f=f[0].strip()
#f = "D2FE28"
#f = "38006F45291200"
#f = "620080001611562C8802118E34"

r = "{0:08b}".format(int(f, 16)).zfill(4*len(f))
print(r)
totalversionsum=0

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
                literalarray.append(value)
                lastindex+=22+length
            else: # next 11 bits are number of sub packets
                length=int(content[7:18],2)
                print(" -> Number of subpackets:",length)
                value,li = decode_packet(content[18:],length)
                literalarray.append(value)
                lastindex+=18+li

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

    return literalarray,lastindex

        
            
print(decode_packet(r,1))

print(totalversionsum)


#501 is too low