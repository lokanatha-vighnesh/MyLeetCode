class Solution {
    public boolean isPalindrome(int x) {
        int result=0;
        int original = x;
        if(x<0) return false;
        while(original != 0){
            int r = original % 10;
            result = result * 10+ r;
            original = original/10;
        }
        return x == result;
    }
}
