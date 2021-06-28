'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

def Two_Sum(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]
