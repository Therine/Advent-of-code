#pull in input
with open ("input") as f:
    lines = f.read()
    #This data is a set of strings right now
    for i in range(0, len(lines)):
        lines[i] = int(lines[i])

# I need to index this list by elf. Each group of numbers before the blank list needs to be summed and the largest sum identified. 
print(lines)
elfCalories = lines[0] + lines[1]
print(elfCalories)

#First, I need to iterate over each measurement in order to 
#for i in range(0, 2261):
#    maxCalories = []
#    while lines[i] != '':
#        elfCalories = lines[i] + lines[i+1]
#    else:
#        maxCalories.append(elfCalories)


#First, I need to iterate over each measurement in order to 
#for i in range(0, 2261):
#    if lines[i] == '':
#        elfCalories = lines[i] + lines[i+1]
#
#    else: maxCalories.append(elfCalories)

#print(maxCalories)
#print(elfCalories)
