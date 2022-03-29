class Solution(object):
    def countCharacters(self, words, chars):
        flag = False
        ans = 0
        for word in words: 
            for char in word: 
                if word.count(char) <= chars.count(char): 
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                ans += len(word)
        return ans
