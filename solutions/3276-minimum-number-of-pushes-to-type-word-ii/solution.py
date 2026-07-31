class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        d = {}
        pushes = {1:[],2:[],3:[],4:[]}
        for i in range(n):
            val = word[i]
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
        a = list(set(word))
        count = 0
        arr = sorted(a, key = lambda x: d[x],reverse=True)
        for i in range(len(a)):
            val = arr[i]
            if count < 8 and val not in pushes[1]:
                pushes[1].append(val)
                count += 1
            elif count >= 8 and count < 16 and val not in pushes[2]:
                pushes[2].append(val)
                count += 1
            elif count >= 16 and count < 24 and val not in pushes[3]:
                pushes[3].append(val)
                count += 1
            elif count >= 24 and val not in pushes[4]:
                pushes[4].append(val)
                count += 1
        print(d)
        print(pushes)
        ans = 0
        for i in range(1,5):
            for j in pushes[i]:
                ans += d[j]*i

        return ans
