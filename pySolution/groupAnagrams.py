class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        ans = []
        for i in strs:
            key = tuple(sorted(i))
            if key in dict:
                dict.get(key).append(i)
            else:
                dict[key] = [i]
        for i in dict.values():
            ans.append(i)
        return ans


s = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(s)