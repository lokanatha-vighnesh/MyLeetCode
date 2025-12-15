class Solution(object):
    def getDescentPeriods(self, prices):
        prices.append(10000)
        n = len(prices)
        count = len(prices)-1
        if count == 1:
            return 1
        left = 0
        right = 1
        answer = []
        while left < n and right < n:
            if prices[right-1]-prices[right] == 1:
                right += 1
            else:
                answer.append(prices[left:right])
                left = right
                right += 1
        ans = 0
        for i in answer:
            ans += len(i)*(len(i)+1)//2
        return ans

        
        

