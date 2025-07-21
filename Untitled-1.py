# Given an array nums of integers, return how many of them contain an even number of digits
# example: nums = [12,1,1221, 1334, 13333] 
# output: 3 
# given that 12, 1221, and 1334 are the event number of digits 


l=[12,1,1221,1334,13333]
count = 0

for n in l:
    if len(str(n))  % 2 == 0:
        count += 1
        
    print ("true")
else:
    print ("false")
print("no of evens in array: ", count)


