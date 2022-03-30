class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        for i in range(len(nums)):
            x = nums[i]
            right -= x
            if left == right:
                return i
            left += x
        return -1
        
            
