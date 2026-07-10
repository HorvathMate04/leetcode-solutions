"""The string "PAYPALISHIRING" is written in a zigzag pattern on a 
given number of rows like this: (you may want to display this pattern 
in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1: return s
        result = [[] for _ in range(numRows)]
        direction = -1
        current = 0
        for i in range(len(s)):
            result[current].append(s[i])
            if(current == 0 or current == numRows-1): direction = direction*-1
            current += direction
        return "".join(sum(result, []))