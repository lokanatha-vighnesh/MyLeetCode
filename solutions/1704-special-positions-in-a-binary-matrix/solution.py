class Solution(object):
    def numSpecial(self, mat):
        rows = []
        cols = []
        for i in mat:
            rows.append(i.count(1))
        for i in range(len(mat[0])):
            count = 0
            for j in range(len(mat)):
                if mat[j][i] == 1:
                    count += 1
            cols.append(count)
        print(rows,cols)
        answer = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    answer += 1
                else:
                    continue
        return answer  
