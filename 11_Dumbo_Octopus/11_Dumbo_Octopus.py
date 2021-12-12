import numpy as np

lines = open("input.txt").readlines()

energy_levels=[]

#convert puzzle input file into integer numpy array
for i in lines:
    i=i.strip()
    row=[]
    for nums in i:
        row.append(nums)
    energy_levels.append(row)

energy_levels=np.array(energy_levels,dtype=int)

total_flashcount=0 # total count of flashed octopuses


def makestep(energy_array):
    global total_flashcount
    energy_array=energy_array+1 #add 1 to whole array
    while True:
        flash_positions=np.argwhere(energy_array>9) # find all octopuses with an energy greater than 9
        if len(flash_positions)==0: # if there are none the step is completed
            break
        for flashes in flash_positions:
            total_flashcount+=1 # increase total counter of flashes by 1
            energy_array[flashes[0],flashes[1]]=0 # set energy of flashed octopus to 0

            ymin=-1 if flashes[0]>0 else 0 # check if y position of octopus is at least 1 (check if not on the left edge of array)
            ymax = 2 if (flashes[0]<(energy_array.shape[0])-1) else 1 # check if y position of octopus isn't on the right edge

            xmin =-1 if flashes[1]>0 else 0 # check if x position of octopus is at least 1 (False for first row of array)
            xmax= 2 if (flashes[1]<(energy_array.shape[1])-1) else 1 # check if x position of octopus isn't in the last array row

            for x in range(xmin,xmax):
                for y in range(ymin,ymax):
                    if energy_array[flashes[0]+y,flashes[1]+x] != 0: #if energy of octopus isn't 0 (just flashed) 
                        energy_array[flashes[0]+y,flashes[1]+x]+=1 # increase it by 1

    return energy_array


current_step=0
needtocalcparttwo=True
## Part One ##
for step in range(100):
    current_step+=1
    energy_levels=makestep(energy_levels)
    if needtocalcparttwo and (sum(sum(energy_levels)))==0: #check if all octopuses flashed and if it was the first time this happend
        all_flash_step=current_step
        needtocalcparttwo=False
    

print("Part one:",total_flashcount)
            
## Part Two ##

while needtocalcparttwo: # 
    current_step+=1
    energy_levels=makestep(energy_levels)
    
    if (sum(sum(energy_levels)))==0: # check if all octopuses flashed
        all_flash_step=current_step
        break


print("Part two:",all_flash_step)

