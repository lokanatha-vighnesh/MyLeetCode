class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        arr = []
        s = 0
        for i in n:
            if i != '0':
                s += int(i)
                arr.append(i)
            else:
                continue
        val = "".join(arr) if len(arr) > 0 else '0'

        return int(val) * s
