class Solution(object):
    def numSub(self, s):
        count = 0
        k = 0
        for i in s:
            if i == '0':
                count += (k*(k+1))//2
                k=0
            else:
                k+=1
        count+=(k*(k+1))//2
        count %= 10**9 + 7
        return count
        
