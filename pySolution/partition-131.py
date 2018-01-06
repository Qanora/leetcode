class Solution:
    def partition(self, s):
        self.current_list = []
        self.final_ans = []
        self.dfs(s)
        print(self.final_ans)

    def dfs(self, s):
        if not s:
            self.final_ans.append(self.current_list[:])
            return
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.current_list.append(s[:i+1])
                self.dfs(s[i+1:])
                self.current_list.pop()

    def isPalindrome(self, s):
        temp = ""
        for val in s:
            if val.isalnum():
                temp += val.lower()

        for i in range(int(len(temp)/2)):
            if temp[i] != temp[-i-1]:
                return False
        return True

Solution().partition("")

