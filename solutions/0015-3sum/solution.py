class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        i = 0
        n = len(nums)
        while i < n-1:
            num1 = nums[i]
            j = i + 1
            k = n-1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
            else:
                while j < k:
                    a = [num1,nums[j],nums[k]]
                    s = sum(a)
                    if s == 0:
                        ans.append(a)
                        j += 1
                        k -= 1    
                        while j > i+1 and j<k and nums[j] == nums[j-1]:
                            j += 1
                        while k < n-2 and j<k and nums[k] == nums[k+1]:
                            k -= 1
                    elif s < 0:
                        j += 1
                    else:
                        k -= 1
                i += 1

        return ans
            

