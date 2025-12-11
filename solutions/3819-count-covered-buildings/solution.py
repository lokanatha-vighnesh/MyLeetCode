class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        if n < 3:
            return 0
        m = len(buildings)
        if m < 5:
            return 0
        x={}
        y={}
        count = 0
        for i in range(m):
            if buildings[i][0] not in x:
                x[buildings[i][0]] = [buildings[i][1]]
            else:
                x[buildings[i][0]].append(buildings[i][1])

            if buildings[i][1] not in y:
                y[buildings[i][1]] = [buildings[i][0]]
            else:
                y[buildings[i][1]].append(buildings[i][0])
        for i,k in x.items():
            k_x = [min(k),max(k)] if min(k) != max(k) else [min(k),min(k)]
            x[i] = k_x
        
        for i,k in y.items():
            k_y = [min(k),max(k)] if min(k) != max(k) else [min(k),min(k)]
            y[i] = k_y
        for i in buildings:
            x_i = i[0]
            y_i = i[1]
            if x_i in x and y_i > x[x_i][0] and y_i < x[x_i][1] and y_i in y and x_i > y[y_i][0] and x_i < y[y_i][1]:
                count += 1
            else:
                continue
        
        return count
