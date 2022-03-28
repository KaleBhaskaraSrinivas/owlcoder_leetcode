class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        cur_sum, max_sum = 0, 0
        for num in nums:
            cur_sum = max(0, cur_sum + num)
            max_sum = max(cur_sum, max_sum)
        return max_sum
