import math

class Solution(object):
    def countTriples(self, n):
        count = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (math.sqrt(i*i + j*j)).is_integer() and (math.sqrt(i*i + j*j)) <= n:
                    count+=1
                else:
                    continue
        return count
