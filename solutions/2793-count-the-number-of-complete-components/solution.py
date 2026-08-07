class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i:set([i]) for i in range(n)}
        
        for i,j in edges:
            nodes[i].add(j)
            nodes[j].add(i)
        
        group = {}
        for i,j in nodes.items():
            
            key = frozenset(j)
            if key not in group:
                group[key] = []
            group[key].append(i)

        print(group, nodes)
        count = 0
        for i,j in group.items():
            if set(i) == set(j):
                count += 1
            else:
                continue


        return count
        
        """ for i in range(n):
            visited = [0]*n
            ans = []
            dfs(i, graph, visited, ans)"""

