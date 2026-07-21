class Solution(object):
    def allOnes(self,a):
        return len(a) == a.count('1')
    def allZeros(self,a):
        return len(a) == a.count('0')
    def maxActiveSectionsAfterTrade(self, s):
        if len(s) <= 2:
            return s.count('1')
        if self.allOnes(s):
            return len(s)
        if self.allZeros(s):
            return 0
        arr = []
        idx = 0
        t = '1' + s + '1'
        for i in range(0,len(t)-1):
            if t[i] != t[i+1]:
                arr.append(t[idx:i+1])
                idx = i+1
            if i == len(t)-2:
                arr.append(t[idx:i+2])
        num = []
        for i in arr:
            num.append(len(i) if self.allOnes(i) else -len(i))
        m = 0
        for i in range(2,len(num)-1):
            if num[i-1] < 0 and num[i+1] < 0:
                m = max(m,abs(num[i-1])+abs(num[i+1]))
        ans = 0
        for i in num:
            ans += i if i > 0 else 0
        
        return ans+m-2
