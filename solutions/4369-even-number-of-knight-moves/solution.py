class Solution(object):
    def canReach(self, start, target):
        """
        :type start: List[int]
        :type target: List[int]
        :rtype: bool
        """
        return (sum(start)%2==0 and sum(target)%2==0) or (sum(start)%2==1 and sum(target)%2==1)
