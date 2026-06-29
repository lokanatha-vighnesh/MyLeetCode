class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(patterns)
        count = 0
        for i in patterns:
            if i not in word:
                count += 1
            
        return n-count
