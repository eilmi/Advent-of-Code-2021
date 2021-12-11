import numpy as np

lines = open("input.txt").readlines()

energy_levels=[]

for i in lines:
    i=i.strip()
    row=[]
    for nums in i:
        row.append(nums)
    energy_levels.append(row)

energy_levels=np.array(energy_levels,dtype=int)
energy_levels


total_flashcount=0


def makestep(energy_array):
    global total_flashcount
    energy_array=energy_array+1
    while True:
        flash_positions=np.argwhere(energy_array>9)
        if len(flash_positions)==0:
            break
        for flashes in flash_positions:
            total_flashcount+=1
            energy_array[flashes[0],flashes[1]]=0

            ymin=-1 if flashes[0]>0 else 0
            ymax = 2 if (flashes[0]<(energy_array.shape[0])-1) else 1

            xmin =-1 if flashes[1]>0 else 0
            xmax= 2 if (flashes[1]<(energy_array.shape[1])-1) else 1

            for x in range(xmin,xmax):
                for y in range(ymin,ymax):
                    if energy_array[flashes[0]+y,flashes[1]+x] != 0:
                        energy_array[flashes[0]+y,flashes[1]+x]+=1

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
    

print(total_flashcount)
            
## Part Two ##

while needtocalcparttwo: # 
    current_step+=1
    energy_levels=makestep(energy_levels)
    
    if (sum(sum(energy_levels)))==0: # check if all octopuses flashed
        all_flash_step=current_step
        break


print(all_flash_step)

