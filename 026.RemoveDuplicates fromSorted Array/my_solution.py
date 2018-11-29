class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=1
        while index < len(nums):
            if nums[index] != nums[index-1]:
                index+=1
            else:
                nums.pop(index)
        return len(nums)
            
