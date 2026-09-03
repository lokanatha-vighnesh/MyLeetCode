class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        small = min(nums1)
        if small % 2 == 1:
            return True
        else:
            for i in nums1:
                if i % 2 == 0:
                    continue
                else:
                    return False
            return True
        """ n = len(nums1)
        nums1_odd = []
        nums1_even = []
        for i in range(n):
            v = nums1[i]
            if v % 2 == 0:
                nums1_even.append(v)
            else:
                nums1_odd.append(v)
        odd = min(nums1_odd) if nums1_odd else min(nums1_even)
        even = min(nums1_even) if nums1_even else min(nums1_odd)
        nums2_odd = [0]*n
        nums2_even = [0]*n

        for i in range(n):
            val = nums1[i]
            if val %2 == 0:
                nums2_even[i] = val
                nums2_odd[i] = val-odd
            else:
                nums2_odd[i] = val
                nums2_even[i] = val-even

        odd_true, even_true = True, True
        for i in range(n):
            if nums2_odd[i] % 2 == 1:
                continue
            else:
                odd_true = False
            if nums2_even[i] % 2 == 0:
                continue
            else:
                even_true = False

        return odd_true or even_true
             """
