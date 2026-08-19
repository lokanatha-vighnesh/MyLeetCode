class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_dict = {}
        for i,j in reservedSeats:
            if i in row_dict:
                row_dict[i].append(j)
            else:
                row_dict[i] = [j]
        
        count = (n-len(row_dict))*2
        p1 = {2,3,4,5}
        p2 = {4,5,6,7}
        p3 = {6,7,8,9}
        for row in row_dict.values():
            if not p1.intersection(row):
                count += 1
            elif not p2.intersection(row):
                count += 1
                continue
            if not p3.intersection(row):
                count += 1
        return count
