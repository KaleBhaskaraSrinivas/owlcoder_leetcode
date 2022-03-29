class Solution(object):
    def uniqueMorseRepresentations(self, words):
        d=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        x=[]
        c=0
        for j in words:
            w=j
            s=""
            for i in w:
                s+=d[ord(i)-97]
            if(s not in x):
                x.append(s)
                c+=1
        return c
