"""Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned). """

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = str(abs(x))[::-1]
        result_int = int(result) if x >= 0 else -int(result)
        return 0 if result_int < -2**31 or result_int > 2**31 - 1 else result_int