class Solution(object):
    def checkIfPangram(self, sentence):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        for let in alphabet:
            if let not in sentence:
                return False
        
        return True
