class Solution {
public:
    int addDigits(int num) {
        while (num/10 > 0){
            int dup = 0;
            while(num != 0){
                dup = dup + num % 10;
                num = num / 10;
            }
            num = dup;
        }
        return num;
    }
};
