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
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return mid+1 if len(nums) == 1 else self.searchInsert(nums[mid:], target) + mid
        if nums[mid] > target:
            return mid if len(nums) == 1 else self.searchInsert(nums[:mid], target)