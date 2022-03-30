class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            if nums.count(num) == 1:
                result += num
        
        return result
        
