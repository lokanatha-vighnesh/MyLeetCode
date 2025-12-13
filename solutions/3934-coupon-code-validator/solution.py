import re
class Solution(object):
    def priority(self,business):
            if business == "electronics":
                return 0
            elif business == "grocery":
                return 1
            elif business == "pharmacy":
                return 2
            elif business == "restaurant":
                return 3
            else:
                return 4
    def validateCoupons(self, code, businessLine, isActive):
        '''n = len(code)
        pattern = r'^[a-zA-Z/d_]+$'
        answer = []
        valid_business = ("electronics","grocery","pharmacy","restaurant")
        for i in range(n):
            if businessLine[i] in valid_business and isActive[i]:
                out = re.findall(pattern,code[i])
                if out:
                    answer.append(code[i])
                else:
                    continue
            else:
                continue '''
        zipped = zip(code,businessLine,isActive)
                
        answer = []
        pattern = r'^[A-Za-z0-9_]+$'
        valid_business = ("electronics","grocery","pharmacy","restaurant")
        for i in zipped:
            if i[2] and i[1] in valid_business and i[0]:
                out = re.findall(pattern,i[0])
                if out:
                    answer.append(i)
                    
        if answer:
            sorted_answer = sorted(answer,key = lambda x : (self.priority(x[1]),x[0]))
            print(sorted_answer)
            c,l,a = zip(*sorted_answer)
        else:
            return answer
        return c
