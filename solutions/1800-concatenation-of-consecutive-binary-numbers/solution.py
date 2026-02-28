class Solution(object):
    def concatenatedBinary(self, n):
        modulo = (10**9+7)
        answer = ''
        for i in range(1,n+1):
            answer += bin(i)[2:]
        return (int(answer,2)%modulo)
        
