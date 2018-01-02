from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        new_wordList = {}

        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                new_wordList[s] = new_wordList.get(s, []) + [word]

        visitList = deque([(beginWord,1)])
        visist = set()
        #print(new_wordList)

        while visitList:
            #print("visitList ",visitList)
            word, deep = visitList.popleft()
            if word not in visist:
                visist.add(word)
                if word == endWord:
                    return deep
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    new_list = new_wordList.get(s, [])
                    #print(s,new_list)
                    for temp in new_list:
                        if temp not in visist:
                            visitList.append([temp, deep+1])
        return 0

s = Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
print(s)