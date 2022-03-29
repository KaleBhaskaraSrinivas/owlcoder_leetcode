class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l1, l2 = list(s), list(t)
        for e in l1:
            l2.remove(e)
        return "".join(l2)
        # return "".join([ele for ele in t if ele not in s])
 
    def findTheDifference2(self, s, t):
        code = 0
        for ch in s:
            code ^= ord(ch)
        for ch in t:
            code ^= ord(ch)
        return chr(code)
 
    def findTheDifference3(self, s, t):
        ans = 0
        for c in s+t:
            ans ^= ord(c)
        return chr(ans)
 
 
if __name__ == '__main__':
    sol = Solution()
    s = "abcd"
    t = "abcde"
    print sol.findTheDifference(s, t)
    print sol.findTheDifference2(s, t)
