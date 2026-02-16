class Solution(object):
    def reverseBits(self, n):
        i = abs(n)
        s = ''
        while i != 0:
            if i % 2 == 0: 
                s = '0' + s
                i //= 2
            else:
                s = '1' + s
                i //= 2
            
        
        while len(s) < 31:
            s = '0' + s
            
        if n < 0:
            num = ('1'+s)[::-1]
        else:
            num = ('0'+s)[::-1]
        sign = 1
    
        if num[0] == '1':
            sign = -1
        act_num = num[1:][::-1]
        sums = 0
        j=0
        for i in act_num:
            sums += (int(i)*(2**j))
            j+=1
        return sums*sign
