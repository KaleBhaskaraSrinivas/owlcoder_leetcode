class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<r:
            mid=(l+r)//2
            if sum(math.ceil(el/mid) for el in piles)>h:
                l=mid+1
            else:
                r=mid
        return l
