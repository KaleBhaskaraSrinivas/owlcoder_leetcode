class Solution(object):
    def sortSentence(self, s):
        arr = s.split(" ");
        res  = [0]*len(arr)
        for i in arr:
            idx = i[len(i)-1];
            res[int(idx)-1] = i[0:len(i)-1]
        return " ".join(res)
