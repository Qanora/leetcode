class Solution:
    def isPalindrome(self, s):
        temp = ""
        for val in s:
            if val.isalnum():
                temp += val.lower()

        for i in range(int(len(temp)/2)):
            if temp[i] != temp[-i-1]:
                print(temp[i],temp[-i-1])
                return False
        return True

s = Solution().isPalindrome("")
print(s)