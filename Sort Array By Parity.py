class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr = deque()
        for i in nums:
            if i%2:
                arr.append(i)
            else:
                arr.appendleft(i)
        return arr
        
        
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i%2==0:
                res.insert(0,i)
            else:
                res.append(i)
        return res
        
