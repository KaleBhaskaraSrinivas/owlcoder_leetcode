class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = max(nums)
        if len(nums) < 2:
            return 0    
        else:    
            c = nums.index(x)
            s =  nums[:c] + nums[c+1:]
            for i in s:
                newi = 2 * i
                if newi > x:
                    return -1
            return nums.index(x)
        
