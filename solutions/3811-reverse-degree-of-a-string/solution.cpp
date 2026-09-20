class Solution {
public:
    int reverseDegree(string s) {
        int ans = 0;
        int n = s.length();
        for(int i=0;i<n;i++){
            int val = int(s[i]);
            ans += ((26-val+97)*(i+1));
        }
        return ans;
    }
};
