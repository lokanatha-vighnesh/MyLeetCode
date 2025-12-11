class Solution(object):
    def numSteps(self, s):
        n = len(s)
        new_s = int(s,2)
        count = 0
        while new_s != 1:
            if new_s % 2 == 1:
                new_s += 1
            else:
                new_s /= 2
            count += 1
        return count
