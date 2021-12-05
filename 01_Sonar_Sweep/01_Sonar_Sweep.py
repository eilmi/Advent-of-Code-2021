f = open("01_Sonar_Sweep/depth_measurements.txt").readlines()

print ("Part One:")

incs=-1
prev=0
for i in f:
    n = int(i)
    if n > prev:
        incs=incs+1
    prev=n

print(incs)


# Part Two
print ("Part Two:")

numbers = [int(i, base=10) for i in f]

incs=-1
prev=0
for i in range(len(numbers)-2):
    sum = numbers[i]+numbers[i+1]+numbers[i+2]
    if sum > prev:
        incs+=1
    prev=sum

print(incs)