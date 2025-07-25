class Solution {
    int maxnum(int[] a,int b){
        int x = b;
        for(int j = 0;j<a.length;j++){
            if(a[j] > x){
                x = a[j];
            }
        }
        return x;
    }
    public int maxSum(int[] nums) {
        int result = 0;
        ArrayList<Integer> list = new ArrayList<>();
        int state = 0;
        int min = Integer.MIN_VALUE;
        for (int num : nums) {
            if (!list.contains(num)) {
                if (num>=0){
                    list.add(num);
                    result += num;
                }else{
                    state++;
                    if (num > min){
                        min = num;
                    }
                }
            }
        }
        
        return (state == nums.length)?min:result;
    }
}
