class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left, right = 0, 0
        left_sum, right_sum = 0, 0

        mid = n//2
        for i in range(mid):
            if num[i] == '?':
                left += 1
            else:
                left_sum += int(num[i])
            if num[mid+i] == '?':
                right += 1
            else:
                right_sum += int(num[mid+i])


        
        print(left, right, left_sum, right_sum)
        if left == 0 and right == 0:
            return left_sum != right_sum
        diff = (right-left)
        return (left_sum-right_sum) != diff*4.5
        if diff % 2 == 0:
            if (left_sum-right_sum) >= diff*4.5:
                return True
            else:
                return False
        else:
            return True

        
