class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones)>1):
            stones.sort()
            x=stones[-1]
            y=stones[-2]
            stones[-1]=(x-y)
            stones.remove(stones[-2])
        return stones[0]
        
        
