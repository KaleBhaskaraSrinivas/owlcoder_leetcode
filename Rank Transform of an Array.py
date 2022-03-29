class Solution(object):
    def arrayRankTransform(self, arr):
        if len(arr)<1: return None
        newarr = sorted(arr)
        orderdict = {newarr[0]:1}
        prev = newarr[0]
        for i in newarr[1:]:
            if i > prev:
                orderdict.setdefault(i,orderdict[prev]+1)
                prev = i
        return [orderdict[i] for i in arr]
