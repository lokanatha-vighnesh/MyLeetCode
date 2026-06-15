class Solution:
    def char2num(self,letter):
        return ord(letter)-97
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for i in words:
            s = 0
            for j in i:
                s += weights[self.char2num(j)]
            s = s%26
            ans = ans + chr(122-s)

        return ans

