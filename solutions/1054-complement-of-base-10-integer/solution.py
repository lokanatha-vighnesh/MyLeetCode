class Solution(object):
    def bitwiseComplement(self, n):
        s=""
        if n == 0:
            return 1
        while n > 0:
            if n % 2 == 0:
                s = '1' + s
            else:
                s = '0' + s
            n /= 2
        num = 0
        for i in s:
            if i == '1':
                num = ((num*2)+1)
            else:
                num *= 2
        return num
        
