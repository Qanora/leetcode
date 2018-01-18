class Solution:
    def compareVersion(self, version1, version2):
        temp1 = [int(v) for v in version1.split('.')]
        temp2 = [int(v) for v in version2.split('.')]
        i = 0
        while i < max(len(temp1), len(temp2)):
            v1 = temp1[i] if i < len(temp1) else 0
            v2 = temp2[i] if i < len(temp2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            i += 1
        return 0

s = Solution().compareVersion("1.0","1")
print(s)