class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        val = requests[0]
        for i in range(1,len(requests)):
            val += abs(requests[i]-requests[i-1])

        return val
