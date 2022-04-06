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
                
