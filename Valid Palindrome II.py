class Solution:
    def validPalindrome(self, s: str) -> bool:
        rev=s[::-1]
        i=0
        j=0
        if s==rev:
            return True
        while s[i]==rev[i]:
            i+=1
        while s[j-1]==rev[j-1]:
            j-=1
        if j==0:
            s=s[i:]
            rev=rev[i:]
        else:
            s=s[i:j]
            rev=rev[i:j]
        if s[1:]==rev[:-1] or s[:-1]==rev[1:]:
            return True
        return False
        
