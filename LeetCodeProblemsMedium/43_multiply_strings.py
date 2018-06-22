"""
https://leetcode.com/problems/multiply-strings/description/
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        isAnswerPositive = True
        if num1[0] == '-':
            isAnswerPositive = not isAnswerPositive
            num1 = num1[1:]
        if num2[0] == '-':
            isAnswerPositive = not isAnswerPositive
            num2 = num2[1:]

        num1 = num1[::-1]
        num2 = num2[::-1]
        lenNum1 = len(num1)
        lenNum2 = len(num2)
        res = [ 0 for i in range(lenNum1 + lenNum2) ]
        i = j = 0
        for i in range(lenNum1):
            for j in range(lenNum2):
                res[i+j] += int(num1[i])*int(num2[j])
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10

        res = res[::-1]
        i = 0
        while i < lenNum2+lenNum1:
            if res[i] != 0:
                break
            i += 1
        if i == lenNum2+lenNum1:
            return "0"
        else:
            res = res[i:]

        res = [str(ch) for ch in res]
        answer = "".join(res) if isAnswerPositive else '-'+"".join(res)
        print answer
        return answer

if __name__ == "__main__":
    x = Solution()
    x.multiply("23", "47")
    x.multiply("2", "-4")
    x.multiply("-2", "-4")
    x.multiply("-26768", "0")

