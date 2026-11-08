class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        o = image[sr][sc]
        if image[sr][sc] == color:
            return image
        def check(x,y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != o:
                return
            
            image[x][y] = color
            check(x-1,y)
            check(x+1,y)
            check(x,y-1)
            check(x,y+1)

        
        check(sr,sc)
        return image
