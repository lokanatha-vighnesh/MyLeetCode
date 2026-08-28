class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        arr = {}
        for i in range(n):
            count = Counter(strs[i])
            val = frozenset(count.items())
            if val in arr:
                arr[val].append(strs[i])
            else:
                arr[val] = [strs[i]]
        
        return list(arr.values())
