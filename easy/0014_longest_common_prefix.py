"""Write a function to find the longest common prefix 
string amongst an array of strings.

If there is no common prefix, return an empty string ""."""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        pref = []
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]): return "".join(pref)
                if strs[0][i] != strs[j][i]:
                    return "".join(pref)
            pref.append(strs[0][i])
        return "".join(pref)