class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = m+n-1;
        int i=n-1;
        int j=m-1;
        while(i>=0 && j>=0){
            if(nums2[i] >= nums1[j]){
                nums1[index] = nums2[i];
                index--;i--;
            }else{
                nums1[index] = nums1[j];
                index--;j--;
            }
        }
        while(i>=0){
            nums1[index] = nums2[i];
            index--;i--;
        }
    }
}
