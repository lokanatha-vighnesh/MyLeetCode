class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low1 = 0
        high1 = len(nums)-1
        left = -1
        while low1 <= high1:
            mid = low1 + (high1 - low1)//2
            if nums[mid] == target:
                left = mid
                high1 = mid - 1
            if nums[mid] >= target:
                high1 = mid - 1
            else:
                low1 = mid + 1

        low2 = 0
        high2 = len(nums)-1
        right = -1
        while low2 <= high2:
            mid = low2 + (high2 - low2)//2
            if nums[mid] == target:
                right = mid
                low2 = mid + 1
            elif nums[mid] >= target:
                high2 = mid - 1
            else:
                low2 = mid + 1
        if not nums:
            return [-1,-1]
        return [left, right] if nums[left]==target and nums[right]==target else [-1,-1]
