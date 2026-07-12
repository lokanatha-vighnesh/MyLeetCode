class Solution(object):
    def letterCombinations(self, digits):
        dictionary = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(digits) <= 1:
            return dictionary[digits]
        else:
            ans = dictionary[digits[0]]
            for i in range(1,len(digits)):
                res = []
                for j in range(len(ans)):
                    for k in range(len(dictionary[digits[i]])):
                        res.append(ans[j]+dictionary[digits[i]][k])
                ans = res

            return ans
        
        
