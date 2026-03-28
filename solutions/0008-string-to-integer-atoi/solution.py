class Solution:
    def myAtoi(self, s: str) -> int:
        
        string = s.strip()
        if not string:
            return 0
        isPositive = False if string[0] == '-' else True
        num = 0
        if isPositive:
            if string[0] == '+':
                string = string[1:]
            for i in range(len(string)):
                v = ord(string[i])
                if v >= 48 and v <= 57:
                    num = ((num * 10) + int(string[i]))
                else:
                    break
        else:
            for i in range(1,len(string)):
                v = ord(string[i])
                if v >= 48 and v <= 57:
                    num = ((num * 10) + int(string[i]))
                else:
                    break
        num = num if isPositive else -num
        if isPositive and num > 2**31-1:
            num = 2**31-1
            return num
        if not isPositive and num < -2**31:
            num = -2**31
            return num
        
        return num
        
        
