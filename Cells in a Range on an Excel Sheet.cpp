class Solution {
public:
    vector<string> cellsInRange(string s) {
        // 
        int c1 = s[0] - 'A' , c2 = s[3] - 'A' ;
        int n1 = s[1] - '0' , n2 = s[4] - '0' ;
        vector<string> res ;
        for (int i = c1 ; i <= c2 ; i ++) {
            string temp = "" ;
            temp += (i + 'A') ;
            for (int j = n1 ; j <= n2 ; j ++) {
                temp += (j + '0') ;
                res.push_back(temp) ;
                temp.pop_back() ;
            }
        } return res ;
    }
};


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(c) + str(r) for c in range(ord(s[0]), ord(s[3]) + 1) for r in range(int(s[1]), int(s[4]) + 1)]
        
