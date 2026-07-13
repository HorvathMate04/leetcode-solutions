"""Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(low, high): 
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return mid+1 if low == high else helper(mid+1, high)
            if nums[mid] > target:
                return mid if low == high else helper(low, mid)
        return helper(0, len(nums)-1)