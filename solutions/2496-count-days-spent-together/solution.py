class Solution:
    def day_number(self,s):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        m = int(s[:2])
        d = int(s[3:])
        count = 0
        for i in range(m-1):
            count += days[i]
        count += d
        return count
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_in = self.day_number(arriveAlice)
        alice_out = self.day_number(leaveAlice)
        bob_in = self.day_number(arriveBob)
        bob_out = self.day_number(leaveBob)
        print(bob_out,alice_out,bob_in,alice_in)
        if (alice_in >= bob_in and alice_in <= bob_out) or (bob_in >= alice_in and bob_in <= alice_out):
            return min(alice_out,bob_out)-max(alice_in,bob_in)+1
        else:
            return 0
