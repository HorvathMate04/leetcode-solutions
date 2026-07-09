"""Given an integer x, return true if x is a palindrome, and false otherwise."""

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        if x < 10: return True
        return x - int(str(x)[::-1]) == 0