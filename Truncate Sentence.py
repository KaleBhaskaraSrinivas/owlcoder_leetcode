class Solution(object):
    def truncateSentence(self, s, k):
        count = 0
        for c in s:
            count += 1
            if c == ' ':
                k -= 1
                if not k:
                    return s[:count-1]
        return s
