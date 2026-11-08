class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sort = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sort[i]:
                count += 1
            else:
                continue

        return count
