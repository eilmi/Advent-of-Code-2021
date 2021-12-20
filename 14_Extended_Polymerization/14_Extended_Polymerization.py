def pairinseration(word,rules,iterations):
    
    pairs={} # Dictionary that stores the number of occurrences of each letter pair

    for i in range(len(word)-1): #check inital word for letter pairs
        st=word[i:i+2] # letter pair
        pairs.update({st:pairs.get(st,0)+1})

    characters={} # Dictionary for storing the number of occurences of each letter
    for i in range(len(word)): #check inital word for letters (iterate over all letters in word)
        characters.update({word[i]:characters.get(word[i],0)+1}) # increase value of dictionary (key = current letter) by 1

    for iters in range(iterations): # perform pair inseration rules for "iterations" times
        changes={} # dictionary which holds the required changes to the "pairs" dict at the and of a inseration 
        for x in pairs: # run for all known pairs of letters
            hm = pairs.get(x) # get number of occurences of this letter pair
            if hm==0: # if this letter pair isnt present right now, skip the steps below
                continue
            else:
                newchar = rules.get(x,"") # get the character which will be inserted between the letter pair
                if newchar=="": # if no rule is available no letter can be inserted so the steps below can be skipped
                    continue
                characters.update({newchar:characters.get(newchar,0)+hm}) # update the number of occurences of the letter which will be inserted between the pair
                changes.update({x:changes.get(x,0)-hm}) # the previous letter pair doesn't exist anymore so the number of occurences of this letter pair must be updated
                newv1=x[0]+newchar # first new letter pair - containing of the first character of the old pair and the newly inserted letter
                newv2=newchar+x[1] # second new letter pair - containing of the newly inserted letter and the second character of the old pair
                changes.update({newv1:changes.get(newv1,0)+hm,newv2:changes.get(newv2,0)+hm}) # update the number of occurences of these two new letter pairs 

        for i in changes: # after all insertions have been made, the changes of occurences of the letter pairs must be inherited into the original dictionary
            hm=changes.get(i,0) #  

            pairs.update({i:pairs.get(i,0)+hm}) # update number of occurences of letter pair in dictionary

    return max(characters.values())-min(characters.values()) # return the difference between the number of occurences of the most and the least common letter

f = open("input.txt").readlines()

rules={}

for i in f[2:]: #create dictionary containing all the insertion rules by iterating over all lines of the input file starting with number 3 (index 2)
    temp = (i.strip().split(" -> ")) #strip and split line of file
    rules.update({temp[0]:temp[1]}) # add current rule to dictionary

print("Part one:",pairinseration(f[0].strip(),rules,10))
print("Part two:",pairinseration(f[0].strip(),rules,40))
