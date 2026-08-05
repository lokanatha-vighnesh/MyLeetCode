class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        methods = {i:[] for i in range(n)}
        
        for i,j in invocations:
            methods[i].append(j)

        visited = [0]*n
        
        def dfs(start,methods,visited):
            if visited[start]:
                return
            
            visited[start] = 1
            for i in methods[start]:
                dfs(i,methods,visited)
        
        
        dfs(k,methods,visited)

        ans1 = []
        ans2 = []
        for i in range(n):
            if visited[i]:
                ans2.append(i)
            else:
                ans1.append(i)
        b = False
        for i,j in invocations:
            if not visited[i] and visited[j]:
                return list(range(n))
        return ans1
