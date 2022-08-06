f = open("depth_measurements.txt").readlines()

numbers = [int(i, base=10) for i in f] # convert string array into int array

############# part one ##################
print ("Part One:")

incs=-1
prev=0
for i in numbers: # iterate over all measurements
    if i > prev: #check if current measurement is larger than the previous one
        incs+=1 # increase counter by 1
    prev=i # make current measurement the previous one

print(incs)

# Part Two
print ("Part Two:")

incs=-1
prev=0
for i in range(len(numbers)-2):
    summe = sum(numbers[i:i+3])
    if summe > prev:
        incs+=1
    prev=summe

print(incs)