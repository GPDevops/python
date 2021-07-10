## codingbat.com
## list2

##Return the number of even ints in the given array.
##Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0


list = [2,1,2,3,4]

for e in list:
    count=0
    for x in list:
        if x%2 == 0:
            count +=1
print(count)


def count_evens(nums):
    count=0
    for x in nums:
        if x%2 == 0:
            count +=1
    return count
    






















    
    




























