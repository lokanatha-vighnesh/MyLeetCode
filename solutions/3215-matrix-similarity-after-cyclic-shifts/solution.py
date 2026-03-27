class Solution:
    def rightShift(self,row : List[int]):
        row = [row[-1]] + row[:-1]
        return row 
    def leftShift(self,col : List[int]):
        col = col[1:] + [col[0]]
        return col
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        duplicate = mat.copy()
        n = len(mat)
        rng = k % len(mat[0])
        for _ in range(rng):
            i = 0
            while i < n:
                if i % 2 == 0:
                    mat[i] = self.leftShift(mat[i])
                else:
                    mat[i] = self.rightShift(mat[i])
                i += 1
        if duplicate == mat:
            return True
        return False
