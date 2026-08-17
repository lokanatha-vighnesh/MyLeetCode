class Solution:
    def isArithemetic(self, num):
        diff = num[1]-num[0]
        for i in range(2,len(num)):
            if num[i]-num[i-1] == diff:
                continue
            else:
                return False
        return True
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        val = 0
        left = 0
        right = 3
        streak = []
        while right <= n:
            arr = nums[left:right]
            if self.isArithemetic(arr):
                right += 1
            else:
                if right - left > 3:
                    streak.append([right-1, left])
                    left = right-2
                    right = left + 3
                elif right - left == 3:
                    right += 1
                    left += 1
        streak.append([right-1, left])
        val = 0
        for i,j in streak:
            v = i-j
            val += ((v-2)*(v-1))//2
        return val
