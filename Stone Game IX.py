class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        mods=[0]*3
        for stone in stones:
            mods[stone%3]+=1
        if mods[0]%2 == 0:
            if mods[1] == 0 or mods[2] == 0: 
                return False
            return True
        else:
            if abs(mods[1]-mods[2]) >= 3: 
                    return True
            return False
    
    

        
