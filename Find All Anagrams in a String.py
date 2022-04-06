class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): 
            return []
        frqs = [0] * 26
        frqp = [0] * 26
        res = []
        for i in range(len(p)):
            frqp[ord(p[i]) - ord('a')] += 1
        i=0
        for j in range(len(s)):
            if j >= len(p):
                frqs[ord(s[i]) - ord('a')] -= 1
                i += 1
            frqs[ord(s[j]) - ord('a')] += 1
            if frqs == frqp:
                res.append(i)
        return res
                
approach-2:
    
 class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def is_Anagram(frqp,frqw):
            for i in range(26):
                if frqp[i]!=frqw[i]:
                    return False
            return True
        frqp=[0]* 26
        frqw=[0]* 26
        n=len(p)
        m=len(s)
        if(n>m):
            return []
        for i in range(n):
            frqp[ord(p[i])-ord('a')]+=1
            frqw[ord(s[i])-ord('a')]+=1
        left=0
        right=n
        l=[]
        while(right<=m):
            if is_Anagram(frqp,frqw):
                l.append(left)
            frqw[ord(s[left])-ord('a')]-=1
            if right<m:
                frqw[ord(s[right])-ord('a')]+=1
            left+=1
            right+=1
        return l   
