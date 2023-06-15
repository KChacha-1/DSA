#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Ex 1
#Input: nums = [1,2,3,1]
#Output: true
#Ex 2
#Input: nums = [1,2,3,4]
#Output: false
#Ex 3
#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true

#approach:
#Convert the list of nums into a list
#base case for quickly checking if length is 1
#possible faster way to sort and then check? and return false if the number is the same as the prev?
#minimum length of nums is 1
#value between -10^9 to 10^9

class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        if len(nums) == 1:
            return false
        return (len(nums) != len(set(nums)))

n1 = [1,2,3,1]
n2 = [1,2,3,4]
n3 = [1,1,1,2,2,2,3,4,2,4,5]
print(Solution().containsDuplicate(n1))
print(Solution().containsDuplicate(n2))
print(Solution().containsDuplicate(n3))





