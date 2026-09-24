class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        int n = nums.size();
        for(int i=0;i<n;i++){
            int val = nums[i];
            int ans = 0;
            while (val > 0){
                ans += val%10;
                val /= 10;
            }
            if (ans == i){
                return i;
            }
        }
        return -1;
    }
};
