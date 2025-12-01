class Solution(object):
    def addBinary(self, a, b):
        intrest = False
        carry = 0
        i=0
        a=a[::-1]
        b=b[::-1]
        s=""
        
        while i < len(a) or i < len(b) or carry:
            num1 = int(a[i]) if i<len(a) else 0
            num2 = int(b[i]) if i<len(b) else 0
            
            sum_s = (num1 + num2 + carry)%2
            carry = (num1 + num2 + carry)//2

            s = str(sum_s) + s

            i+=1
            
        car = str(carry)
        return car+s if car=='1' else s
        
