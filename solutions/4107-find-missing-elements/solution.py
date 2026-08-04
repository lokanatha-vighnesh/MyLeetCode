class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        """ n = len(nums)
        mi = min(nums)
        ma = max(nums)
        arr = []
        while mi <= ma:
            if mi not in nums:
                arr.append(mi)
            mi += 1

        return arr """
        n = len(nums)
        nums.sort()
        a = nums[0]
        b = nums[-1]
        i = 0
        arr = []
        while a <= b:
            if nums[i] == a:
                i += 1
            else:
                arr.append(a)
            a += 1

        return arr
