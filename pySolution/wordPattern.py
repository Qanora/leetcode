class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList = str.split(" ")
        if len(strList) != len(pattern):
            return False
        ans = {}
        temp = []
        for i, val in enumerate(pattern):
            if val not in ans:
                if strList[i] not in temp:
                    temp.append(strList[i])
                else:
                    return False
                ans[val] = strList[i]
            else:
                if ans.get(val) != strList[i]:
                    return False
        return True
s = Solution().wordPattern("abba","dog cat cat dog")
print(s)