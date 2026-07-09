"""Given an integer x, return true if x is a palindrome, and false otherwise."""

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        if x < 10: return True
        return x - int(str(x)[::-1]) == 0
    
"""CHALLENGE: Could you solve it without converting the integer to a string?"""    
    
class Solution(object):
    def isPalindrome2(self, x):
        if x < 0: return False
        if x < 10: return True
        ori = x
        rev = 0
        while ori > 0:
            rev = rev*10 + ori%10
            ori = ori//10
        return x-rev == 0
