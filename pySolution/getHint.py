class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ans = {}
        countA = 0
        countB = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
            else:
                if secret[i] not in ans:
                    ans[secret[i]] = 1
                else:
                    ans[secret[i]] = ans.get(secret[i]) + 1
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if guess[i] in ans and ans.get(guess[i]) > 0:
                    ans[guess[i]] = ans.get(guess[i]) - 1
                    countB += 1
        return str(countA)+"A"+str(countB)+"B"

s = Solution().getHint("10","11")
print(s)

