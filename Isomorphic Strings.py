class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        b, k = {}, set()
        for ch1, ch2 in zip(s, t):
            if ch1 in b:
                if b[ch1] != ch2:
                    return False
            else:
                if ch2 in k:
                    return False
                b[ch1] = ch2
                k.add(ch2)
        return True
