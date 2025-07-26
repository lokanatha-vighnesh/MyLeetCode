class Solution {
    public static int[] shiftZerosToEnd(int[] arr) {
        int lastNonZeroIndex = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                arr[lastNonZeroIndex] = arr[i];
                lastNonZeroIndex++;
            }
        }
        for (int i = lastNonZeroIndex; i < arr.length; i++) {
            arr[i] = 0;
        }
        return arr;
    }
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        int j = 0;
        for(int i = 1;i<n;i++){
            if(nums[i-1] == nums[i]){
                nums[i-1] = nums[i-1]*2;
                nums[i] = 0;j--;
            }else{
                j++;
                continue;
            }
        }
        int arr[] = shiftZerosToEnd(nums);
        return arr;
    }
}
