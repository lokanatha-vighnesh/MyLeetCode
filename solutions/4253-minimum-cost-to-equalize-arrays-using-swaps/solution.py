class Solution(object):
    def minCost(self, nums1, nums2):
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        union = set_nums1.union(set_nums2)

        count1 = {}
        count2 = {}
        count = 0
        for i,j in zip(nums1,nums2):
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
            if j in count2:
                count2[j] += 1
            else:
                count2[j] = 1
        
        for i in union:
            num1 = count1[i] if i in count1 else 0
            num2 = count2[i] if i in count2 else 0
            
            if (num1 + num2)%2 == 1:
                return -1
            else:
                count += (abs(num1-num2))
        return count//4

