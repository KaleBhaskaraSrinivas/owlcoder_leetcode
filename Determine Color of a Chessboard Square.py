class Solution(object):
    def squareIsWhite(self, coordinates):
        if ord(coordinates[0]) % 2 == 1 and ord(coordinates[1]) % 2 == 0:
            return True
        elif ord(coordinates[0]) % 2 == 0 and ord(coordinates[1]) % 2 == 1:
            return True
        else:
            return False
