class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        
        for i in range(1,len(coordinates)-1):
            ab = [coordinates[i][0]-coordinates[i-1][0],coordinates[i][1]-coordinates[i-1][1]]
            bc = [coordinates[i+1][0]-coordinates[i][0],coordinates[i+1][1]-coordinates[i][1]]
            cross = ab[0]*bc[1]-ab[1]*bc[0]
            if cross == 0:
                continue
            else:
                return False
        return True
