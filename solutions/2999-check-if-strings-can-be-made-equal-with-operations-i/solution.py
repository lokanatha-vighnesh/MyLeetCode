class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n = 4
        ori_s1 = s1
        odd_s1 = s1[2] + s1[1] + s1[0] + s1[3]
        even_s1 = s1[0] + s1[3] + s1[2] + s1[1]
        odd_even_s1 = s1[2] + s1[3] + s1[0] + s1[1]

        ori_s2 = s2
        odd_s2 = s2[2] + s2[1] + s2[0] + s2[3]
        even_s2 = s2[0] + s2[3] + s2[2] + s2[1]
        odd_even_s2 = s2[2] + s2[3] + s2[0] + s2[1]

        lis1 = [ori_s1,odd_s1,even_s1,odd_even_s1]
        lis2 = [ori_s2,odd_s2,even_s2,odd_even_s2]

        for i in lis1:
            if i in lis2:
                return True

        return False
