class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return s
        left = self.findPalindrome(s)
        if not left:
            return s[1:][::-1]+s
        else:
            return s[left:][::-1] + s[:left] + s[left:]

    def findPalindrome(self, s):
        mid = len(s)//2
        temp = 0
        while True:
            if mid <= 0:
                return 0
            if mid > 0 and len(s[:mid])+mid < len(s) and s[:mid] == s[mid+1:len(s[:mid])+mid+1][::-1]:
                temp = 1
                break
            if len(s[mid:len(s[:mid])+mid]) < len(s) and s[:mid] == s[mid:len(s[:mid])+mid][::-1]:
                break
            mid -= 1

        if mid < 0:
            return 0
        return mid*2 + temp

s = Solution().shortestPalindrome("abbacd")
print(s)
