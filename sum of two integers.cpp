class Solution {
public:
    int getSum(int a, int b) {
    int c=a&b;
    int sum=a^b;
    while(c!=0)
    {
        a=sum;
        b=(c & 0xffffffff)<<1;
        sum=a^b;
        c=a & b;
    }
    return sum;
    }
};
