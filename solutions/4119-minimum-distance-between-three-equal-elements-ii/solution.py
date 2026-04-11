class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        count = {}
        set_nums = set(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] in count:
                count[nums[i]].append(i)
            else:
                count[nums[i]] = [i]
        ans = float("inf")
        for i in set_nums:
            l = len(count[i])
            if l >= 3:
                for j in range(l-2):
                    ans = min(ans ,2*(max(count[i][j:j+3])-min(count[i][j:j+3])))
            else:
                continue


        return ans if ans != float("inf") else -1
        
