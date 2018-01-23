class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Qa, Qb = 0, 0
        for val in nums:
            LastQa, LastQb = Qa, Qb
            Qa = Qa | (Qb & val)
            Qb = ((~LastQa) & (~LastQb) & val) | ((~LastQa)&LastQb&(~val))
            print(Qa, Qb)

s = Solution().findDuplicate([1,2,3,4,5,6,6])
print(s)