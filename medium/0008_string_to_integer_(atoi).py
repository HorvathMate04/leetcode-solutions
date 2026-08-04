"""Implement the myAtoi(string s) function, 
which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").

Signedness: Determine the sign by checking if the 
next character is '-' or '+', assuming positivity if neither present.

Conversion: Read the integer by skipping leading zeros until a non-digit 
character is encountered or the end of the string is reached. 
If no digits were read, then the result is 0.

Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
then round the integer to remain in the range. Specifically, integers less than -231 
should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.

Return the integer as the final result."""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0: return 0
        mx = 2**31-1
        mn = -2**31
        negative = False
        i = 0
        if s[i] == "-": 
            negative = True
            i += 1
        elif s[i] == "+": i += 1
        result = 0
        while i < len(s) and mn < result < mx:
            if 57 < ord(s[i]) or ord(s[i]) < 48:
                break
            result = result*10 + (ord(s[i])-48)
            i += 1
        if negative: result = result*-1
        if result < mn:
            return mn
        elif result > mx:
            return mx
        return result