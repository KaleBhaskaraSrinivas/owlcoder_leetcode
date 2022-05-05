class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(b % 2 == 0 for b in Counter(nums).values())
        
