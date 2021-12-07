import numpy as np

f = open("input.txt").readlines()

#create 3 dimensional array containing all data
array=[]
for i in f:
    test = i.strip().split(" -> ") # split line at arrow
    line=[]
    for x in test: # run for left and right part of arrow
        coordinates = x.split()[0].split(",") # split each coordinate in x and y value
        coordinates = [int(i, base=10) for i in coordinates] # convert from string to int
        line.append(coordinates) # append coordinates to line (containing of two pairs of an ordered pair)
    array.append(line) # append line to complete array

nparray=np.array(array,dtype=int) # convert in numpy array

# get all diagonal lines
diagonallines=[]
for i in range(nparray.shape[0]):
    line = nparray[i] # store current line of array
    if not(line[0,0]==line[1,0] or line[0,1]==line[1,1]): #check if x1=x2 or y1=y2 is fullfiled
        diagonallines.append(i) # store index of line

# get largest x and y coordinate in all lines
xmax = np.max(nparray[:, :, 0])
ymax = np.max(nparray[:, :, 1])

# create arrays only containing zeros with size of largest coordinates
map = np.zeros([ymax+1,xmax+1])
map2 = np.zeros([ymax+1,xmax+1])

for i in range(nparray.shape[0]): # run for all lines in file
    line = nparray[i] # current working line
    if (i not in diagonallines): # horizontal and vertical line ---- Part one
        for x in range(min(line[0,0],line[1,0]),max(line[0,0],line[1,0])+1): # run for all x coordinates 
            for y in range(min(line[0,1],line[1,1]),max(line[0,1],line[1,1])+1): # run for all y coordinates
                map[y,x]+=1

    else: # diagonal line  ----- Part two
        if (abs(line[0,0]-line[1,0]) == abs(line[0,1]-line[1,1])): # just check if line is exactly 45 degrees (should always be true)
            dx=1 if (line[1,0]-line[0,0]>0) else -1  #check if second point has a greater x-Coordinate than the first point
            dy =1 if (line[1,1]-line[0,1]>0) else -1 # check if second point has a greater y-coordinate than first point

            for i in range(abs(line[0,0]-line[1,0])+1): # run for x and y difference (both the same) between the two points
                map2[line[0,1]+i*dy,line[0,0]+i*dx]+=1 
        else:
            print("Error line is not exactly 45 degrees")


print("Part one:",(map > 1).sum())
print("Part Two:",((map+map2) > 1).sum())