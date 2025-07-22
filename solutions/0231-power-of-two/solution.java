class Solution {
    public boolean isPowerOfTwo(int n) {
        int rem = 0;
        if (n==0 ) return false;
        while(n != 0){
            if(n%2 == 0){
                n /= 2;
            }else{
                if (n == 1){
                    return true;
                }
                return false;
            }
        }
        return true;
    }
}
