# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cht = []
        for c in s.lower():
            if c.isalnum():
                cht.append(c)
        l = len(cht)

        if l > 0:
            mid = l // 2
            left = cht[:mid]
            start = mid + 1 if l % 2 == 1 else mid
            right = cht[start:][::-1]
            return left == right
        else:
            return True
