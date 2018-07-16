"""

"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        lenS1 = len(s1)
        lenS2 = len(s2)
        lenS3 = len(s3)

        if lenS1 + lenS2 != lenS3:
            return False

        # if s1 == "":
        #     return s3 == s2
        # if s2 == "":
        #     return s3 == s1


        T = [ [False]*(lenS2+1) for i in range(lenS1+1)]
        T[0][0] = True

        # Fill up first row and forst col
        for i in range(lenS2):
            if s3[i] == s2[i]:
                T[0][i+1] = T[0][i]
            else:
                T[0][i+1] = False
        for i in range(lenS1):
            if s3[i] == s1[i]:
                T[i+1][0] = T[i][0]
            else:
                T[i+1][0] = False

        self.printMatrix(T)

        for i in range(lenS1):
            for j in range(lenS2):
                T[i+1][j+1] = (T[i][j+1] and s3[i+j+1] == s1[i]) or \
                              (T[i+1][j] and s3[i+j+1] == s2[j])
        self.printMatrix(T)
        return T[-1][-1]


    def printMatrix(self, T):
        print "*"*20
        for i in range(len(T)):
            print T[i]

if __name__ == "__main__":
    x = Solution()
    #x.isInterleave("aab", "axy", "aaxaby")
    #x.isInterleave("aabc", "abad", "aabadabc")
    x.isInterleave("ab", "bc", "babc")