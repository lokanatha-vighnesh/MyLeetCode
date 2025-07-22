class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = 0;
        int currentSum = 0;
        int maxSum = 0;
        Set<Integer> set = new HashSet<>();

        while (right < n) {
            if (!set.contains(nums[right])) {
                currentSum += nums[right];
                set.add(nums[right]);
                maxSum = Math.max(maxSum, currentSum);
                right++;
            } else {
                currentSum -= nums[left];
                set.remove(nums[left]);
                left++;
            }
        }

        return maxSum;
    }
}

