class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cu = [1000]*len(s)
        pos = []
        for i in range(0,len(s)):
            if s[i]==c:
                pos.append(i)
        for j in range(0,len(pos)):
            for k in range(0,len(s)):
                cu[k]=min(cu[k],abs(k-pos[j]))
        return cu
                
      
