class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = deque()
        for i in nums:
            if i%2:
                arr.append(i)
            else:
                arr.appendleft(i)
        return arr
        
