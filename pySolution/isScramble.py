class Solution:
    def isScramble(self, s1, s2):
        left = [s1]
        right = [s2]
        while True:
            tempL = left.pop(0)
            tempR = right.pop(0)
            lenl = len(tempL)
            if lenl < 2:
                break
            left.append(tempL[0:int(lenl/2)])
            right.append(tempR[0:int(lenl/2)])
            left.append(tempL[int(lenl/2):lenl])
            right.append(tempR[int(lenl/2):lenl])
            print("left ", left)
            print("right ", right)
            print("===============================")
Solution().isScramble("great","rgtae")