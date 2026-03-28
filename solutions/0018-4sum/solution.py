class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            for j in range(i+1,n):
                num2 = nums[j]
                k = j + 1
                w = n-1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while k < w:
                    a = [num1,num2,nums[k],nums[w]] 
                    s = sum(a)
                    if s == target:
                        ans.append(a)
                        k += 1
                        w -= 1
                        while k < w and nums[k] == nums[k-1]:
                            k += 1
                        while k < w and nums[w] == nums[w+1]:
                            w -= 1
                    elif s < target:
                        k += 1
                    else:
                        w -= 1

        return ans
