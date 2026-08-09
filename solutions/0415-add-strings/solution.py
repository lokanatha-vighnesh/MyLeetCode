class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1, l2 = len(num1), len(num2)
        carry = 0
        ans = []
        while i < l1 or i < l2 or carry != 0:
            n1 = int(num1[i]) if i < l1 else 0
            n2 = int(num2[i]) if i < l2 else 0

            s = n1 + n2 + carry
            val = s % 10
            carry = s // 10

            ans.append(str(val))
            i += 1

        return "".join(ans)[::-1]


