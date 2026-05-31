class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        sub = [0]*n

        sorted_asteroids = sorted(asteroids)
        for i in range(n):
            if sorted_asteroids[i] <= mass:
                mass += sorted_asteroids[i]
            else:
                return False

        return True

        
