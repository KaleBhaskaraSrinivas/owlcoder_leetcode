class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(0,len(s)):
            for j in range(0,len(s)-i+1):
                if (s[i:i+j] == s[i:i+j][::-1]) and s[i:i+j] !="":
                    c=c+1
        return c
        
