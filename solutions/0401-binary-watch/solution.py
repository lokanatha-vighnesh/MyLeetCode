from itertools import combinations

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        ans = []
        if turnedOn >= 9:
            return ans
        if turnedOn < 0:
            return ans
        if turnedOn == 0:
            return ['0:00']
        hours = [8,4,2,1]
        minutes = [32,16,8,4,2,1]
        
        for m in range(turnedOn+1):
            comb1 = combinations(hours,m)
            comb2 = combinations(minutes,turnedOn-m)
            comb1 = list(comb1)
            comb2 = list(comb2)
            for i in comb1:
                for j in comb2:
                    list_i = list(i)
                    list_j = list(j)
                    h = sum(list_i) if list_i != [] else 0
                    m = ((sum(list_j) if sum(list_j) > 9 else '0'+str(sum(list_j))) if list_j != [] else '00')
                    if h >= 12:
                        continue
                    if int(m) > 59:
                        continue
                    ans.append(('{0}:{1}'.format(h,m)))

        return sorted(ans)
