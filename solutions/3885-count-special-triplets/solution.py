from collections import Counter,defaultdict

class Solution(object):
    def specialTriplets(self, nums):
        n=len(nums)
        count = 0
        
        if n<3:
            return 0
        freq_prev = Counter(nums[:1])
        freq_next = Counter(nums[1:])
        
        for item in range(1,n-1):
            
            target = nums[item]*2
            freq_next[nums[item]]-=1
            
            if target in freq_prev and target in freq_next:
                count += freq_next[target] * freq_prev[target]
            if nums[item] in freq_prev:
                freq_prev[nums[item]]+=1
            else:
                freq_prev[nums[item]] = 1
        return count % (10**9+7)

        
