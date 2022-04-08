class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0);
        stack<int> st;
        for(int i=0; i<n; i++) {
            while(!st.empty() && temperatures[st.top()] < temperatures[i]) {
                int waited = i - st.top();
                result[st.top()] = waited;
                st.pop();
            }
            st.push(i);
        }
        return result;
    }
};
