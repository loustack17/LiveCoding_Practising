# Given two strings s and t, return true if t is an anagram of s, and false otherwise.



class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
         return sorted(s) == sorted(t)


     def isAnagram2(self, s: str, t: str) -> bool:
             if len(s) != len(t):
                return False
             dict_A = {}
             dict_B = {}
             for c in s:
                 if c in dict_A:
                     dict_A[c] += 1
                 else:
                     dict_A[c] = 1
             for c in t:
                 if c in dict_B:
                     dict_B[c] += 1
                 else:
                     dict_B[c] = 1

             return dict_A == dict_B
