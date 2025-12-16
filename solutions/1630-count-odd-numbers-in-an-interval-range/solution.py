class Solution(object):
    def countOdds(self, low, high):
        if (high - low + 1) % 2 == 0:
            return (high - low + 1) // 2
        else:
            if high % 2 == 0:
                return ((high - low + 1) // 2)
            else:
                return ((high - low + 1) // 2)+1
        
        
