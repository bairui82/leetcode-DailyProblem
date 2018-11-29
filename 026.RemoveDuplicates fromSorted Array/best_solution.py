class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l<=1:
            return l
        index = 0
        for i in range(0,l-1):
            if nums[i]!=nums[i+1]:
                nums[index+1]=nums[i+1]
                index+=1
        return index+1
            
