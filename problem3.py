class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        start = 0
        mx = 0

        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char]+1

            seen[char] = i

            if i-start+1 > mx:
                mx = i-start+1

        return mx