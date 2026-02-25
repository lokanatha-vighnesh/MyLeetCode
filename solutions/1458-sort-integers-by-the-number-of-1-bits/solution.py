class Solution(object):
    def sortByBits(self, arr):
        count = {}
        for i in range(len(arr)):
            ones = bin(arr[i]).count('1')
            if ones in count:
                count[ones].append(arr[i])
                
            else:
                count[ones] = [arr[i]]
        
        sorted_ones = sorted(count.keys())
        answer = []
        for i in range(len(sorted_ones)):
            answer.extend(sorted(count[sorted_ones[i]]))
        
        return answer



        
