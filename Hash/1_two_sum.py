# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            remaining = target - num

            for j in range(i+1, len(nums)):
                if remaining == nums[j]:
                    return [i, j]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:

        match = {}
        for i, num in enumerate(nums):
            remaining = target - num

            if remaining in match:
               return [match[remaining], i]

            match[num] = i
