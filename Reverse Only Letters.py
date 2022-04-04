class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        head, tail = 0, len(s)-1
        res = list(s)
        while head < tail:
            if not res[head].isalpha():  # head index is not alphabet, move head forward
                head += 1
            elif not res[tail].isalpha():  # tail index is not alphabet, move tail backward
                tail -= 1
            else:
                res[head], res[tail] = res[tail], res[head]  # exchange position
                head += 1
                tail -= 1
        return ''.join(res)
