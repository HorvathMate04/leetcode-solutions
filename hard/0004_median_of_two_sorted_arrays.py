"""Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))."""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newArray = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                newArray.append(nums1[i])
                i += 1
            else:
                newArray.append(nums2[j])
                j += 1
        if i < len(nums1):
            newArray = newArray + nums1[i::]
        elif j < len(nums2):
            newArray = newArray + nums2[j::]
        lngth = len(newArray)
        if lngth % 2 != 0:
            return newArray[lngth//2]
        else:
            return (newArray[lngth//2-1] + newArray[lngth//2])/2