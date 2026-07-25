"""Given two integers, num and t. A number x is achievable 
if it can become equal to num after applying the following 
operation at most t times:

Increase or decrease x by 1, and simultaneously 
increase or decrease num by 1.
Return the maximum possible value of x."""

class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return t*2 + num