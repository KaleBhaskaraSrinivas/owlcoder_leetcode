class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in arr:
            if i in target:
                target.remove(i)
        if len(target)>0:
            return False
        else:
            return True
        
