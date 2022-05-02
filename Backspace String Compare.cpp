class Solution {
public:
    string backspace(string x){
        string y="";
        stack<char>st;
        for(int i=0;i<x.size();i++){
            if(x[i]=='#'){
                if(!st.empty()){
                    st.pop();
                }
            }
            else{
                st.push(x[i]);
            }
        }
        while(!st.empty()){
            y+=st.top();
            st.pop();
        }
        return y;
        
    }
    bool backspaceCompare(string s, string t) {
         if(backspace(s)==backspace(t)){
            return true;
        }
        return false;
        
    }
};
