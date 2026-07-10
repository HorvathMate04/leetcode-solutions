"""Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
            }
        opened = []
        for char in s:
            if char in pairs.keys():
                opened.append(char)
            elif len(opened) == 0:
                return False
            elif char == pairs[opened[-1]]:
                opened.pop()
            else:
                return False
        return len(opened) == 0
        