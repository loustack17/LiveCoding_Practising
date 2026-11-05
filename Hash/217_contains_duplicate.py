# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        found = set()

        for n in nums:
            if n in found:
                return True
            found.add(n)
        return False
