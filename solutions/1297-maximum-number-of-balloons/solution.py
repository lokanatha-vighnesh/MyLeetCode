class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = ['b','a','l','o','n']
        char = {'b':0,
                'a':0,
                'l':0,
                'o':0,
                'n':0}
        for i in text:
            if i in s:    
                char[i] += 1
            else:
                continue
        char['l'] //= 2
        char['o'] //= 2
        print(char.values())
        return min(char.values())
