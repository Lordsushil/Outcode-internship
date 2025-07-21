

# Given an array nums of integers, return how many of them contain an even number of digits
# example: nums = [12,1,1221, 1334, 13333] 
# output: 3 
# given that 12, 1221, and 1334 are the event number of digits 
#...................................................................................................................................................................

# l=[12,1,1221,1334,13333]
# count = 0

# for n in l:
#     if len(str(n))  % 2 == 0:
#         count += 1
        
#         print ("true")
#     else:
#         print ("false")
#     print("no of evens in array: ", count)

#...................................................................................................................................................................

# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

# Return true if it is possible. Otherwise, return false.

# example 1 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.


# example 2 
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].


#...................................................................................................................................................................

s = input("Enter list: ")
s = s.strip("[]")
l = [x.strip().strip("'\t\"") for x in s.split(",")]

n = int(input("enter n: "))
if len(l) % n != 0:
    print("Array formation is not possible")
else:
    for i in range(0, len(l), n):
        group = l[i:i+n] 
        print("True")
        print("Group:",  group )
        
