class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        loc_max = glo_max = 0
        for i in range(len(nums)):
            if nums[i] == 1: 
                loc_max += 1
            elif nums[i] != 1:
                glo_max = max(glo_max, loc_max)
                loc_max = 0  
                
        return max(glo_max, loc_max)
