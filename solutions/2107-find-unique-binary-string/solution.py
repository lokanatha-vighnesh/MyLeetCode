class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        string = ""
        for i in range(len(nums[0])):
            string += '0' if nums[i][i] == '1' else '1'
        return string
