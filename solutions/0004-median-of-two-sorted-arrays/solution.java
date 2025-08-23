class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length,n2 = nums2.length;
        ArrayList<Integer> arr = new ArrayList<>();
        int i=0,j=0;
        while (i < n1 && j < n2) {
            if (nums1[i] <= nums2[j]) {
                arr.add(nums1[i++]);
            } else {
                arr.add(nums2[j++]);
            }
        }

        // Add remaining elements from nums1
        while (i < n1) {
            arr.add(nums1[i++]);
        }

        // Add remaining elements from nums2
        while (j < n2) {
            arr.add(nums2[j++]);
        }
        return arr.size()%2==0?(arr.get(arr.size()/2)+arr.get((arr.size()/2)-1))/2.0:
        arr.get(((arr.size())/2));
    }
}
