"""A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution(object):
    def isPalindrome(self, s):
        cnt1 = 0
        cnt2 = len(s)-1
        while cnt1 < len(s)-1:
            while cnt1 < len(s)-1 and not s[cnt1].isalnum():
                cnt1 += 1
            while cnt2 > 0 and not s[cnt2].isalnum():
                cnt2 -= 1
            if cnt2 <= cnt1:
                break
            if s[cnt1].lower() != s[cnt2].lower():
                return False
            cnt1 += 1
            cnt2 -= 1
        return True