"""You are given an integer n.

Define its mirror distance as: abs(n - reverse(n))​​​​​​​ 
where reverse(n) is the integer formed by reversing the digits of n.

Return an integer denoting the mirror distance of n​​​​​​​.

abs(x) denotes the absolute value of x."""

class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        return abs(n-int(str(n)[::-1]))