class Solution(object):
    def numberOfseats(self, seats):
        count = 0
        for i in range(len(seats)):            
            if seats[i]=="S":
                count += 1
        return count
    def numberOfWays(self, corridor):
        n = len(corridor)
        left = 0
        left_set = False
        right  = 0
        segment = []
        i = 0
        s_count = 0
        while i < n:
            letter = corridor[i]
            if letter == 'S':
                s_count += 1
                if not left_set:
                    left = i
                    right == left
                    left_set = not left_set
                else:
                    right = i
                    segment.append([left,right])
                    left_set = not left_set
            else:
                if not left_set:
                    left += 1
                right += 1
            i+=1
        if s_count % 2 == 1:
            return 0
        elif s_count == n:
            return 1
        elif s_count == 0:
            return 0
        sums = 1
        if len(segment)==1:
            return 1
        for i in range(1,len(segment)):
            cout = segment[i][0] - segment[i-1][1]
            sums *= (cout)
        
        return sums % (10**9+7)

