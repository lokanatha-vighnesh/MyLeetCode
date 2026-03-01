class Solution(object):
    def minPartitions(self, n):
        if len(n) == 1:
            return int(n)
        else:
            max_num = 0
            for i in n:
                val = int(i)
                if val > max_num:
                    max_num = val
                else:
                    continue

        return max_num

