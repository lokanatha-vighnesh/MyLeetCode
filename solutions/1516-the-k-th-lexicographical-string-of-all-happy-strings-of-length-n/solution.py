class Solution(object):
    def getHappyString(self, n, k):
        total_strings = 3*(2**(n-1))
        if total_strings < k:
            return ""
        
        queue = ['a', 'b', 'c']

        if n == 1:
            return queue[k-1]

        for _ in range(n - 1):
            next_level = []
            for s in queue:
                last_char = s[-1]
                
                if last_char == 'a':
                    next_level.append(s + 'b')
                    next_level.append(s + 'c')
                elif last_char == 'b':
                    next_level.append(s + 'a')
                    next_level.append(s + 'c')
                elif last_char == 'c':
                    next_level.append(s + 'a')
                    next_level.append(s + 'b')
            
            queue = next_level
        return queue[k-1]
