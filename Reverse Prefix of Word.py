class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        x = word.index(ch)+1
        return (word[:x][::-1] + word[x:])
       
        
