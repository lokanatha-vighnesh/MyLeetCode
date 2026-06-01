class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)
        cost = sorted(cost,reverse=True)
        total = 0
        i=0
        while i < len(cost):
            if i > len(cost)-2:
                total += sum(cost[i:])
                break
            else:
                total += cost[i] + cost[i+1]
                i += 3
        return total
