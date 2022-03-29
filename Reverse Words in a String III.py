class Solution(object):
    def reverseWords(self, s):
        words=s.split()
        newords=[]
        for word in words:
            newords.append(word[::-1])
        return " ".join(newords)
