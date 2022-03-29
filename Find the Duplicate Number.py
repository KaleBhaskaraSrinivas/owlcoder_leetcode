class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        low=0
        h=len(nums)
        while low<=h:
            m=(low+h)>>1
            if m==nums[m] and (m==nums[m-1]):
                return m
                break
            elif nums[m]>m:
                low=m+1
            else:
                h=m-1
