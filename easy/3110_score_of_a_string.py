"""You are given a string s. The score of a string is 
defined as the sum of the absolute difference between 
the ASCII values of adjacent characters.

Return the score of s."""

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        for i in range(0, len(s)-1):
            value += abs(ord(s[i]) - ord(s[i+1]))
        return value