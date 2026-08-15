class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dic = defaultdict(int)
        left = 0
        ans = float('inf')
        for right in range(n):
            dic[nums[right]] += 1

            while dic[nums[right]] > 1:
                dic[nums[left]] -= 1
                ans = min(ans, right-left)
                left += 1

        return ans <= k
