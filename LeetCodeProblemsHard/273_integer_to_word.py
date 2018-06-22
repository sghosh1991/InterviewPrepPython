"""
https://leetcode.com/problems/integer-to-english-words/description/

https://www.programcreek.com/2014/05/leetcode-integer-to-english-words-java/
"""

class Solution(object):

    def __init__(self):
        self.word_by_number = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

    def convert(self, num):
        res = []
        if num >= 100:
            extra = num/100
            num %= 100
            res.append(" " + self.word_by_number[extra] + " Hundred")

        if num > 0:
            if num <= 20:
                res.append(" " + self.word_by_number[num])
            else:
                tens = num/10
                res.append(" " + self.word_by_number[tens*10])
                num %= 10
                if num > 0:
                    res.append(" " + self.word_by_number[num])

        return "".join(res)

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []

        if num == 0:
            return "Zero"

        if num >= 1000000000:
            extra = num/1000000000
            num %= 1000000000
            res.append(self.convert(extra) + " Billion")

        if num >= 1000000:
            extra = num/1000000
            num %= 1000000
            res.append(self.convert(extra) + " Million")

        if num >= 1000:
            extra = num/1000
            num %= 1000
            res.append(self.convert(extra) + " Thousand")

        if num > 0:
            res.append(self.convert(num))


        res = "".join(res)
        return res.strip()

if __name__ == "__main__":
    x = Solution()
    print x.numberToWords(1234)
    print x.numberToWords(1000000)
    print x.numberToWords(0)
    print x.numberToWords(100)
    print x.numberToWords(1004)
    print x.numberToWords(1000)
    print x.numberToWords(123456789234)
    print x.numberToWords(12354)