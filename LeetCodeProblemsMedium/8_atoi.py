"""

"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.strip()
        if len(str) == 0:
            return 0

        INT_MAX = (2**31 - 1)
        INT_MIN = -(INT_MAX + 1)

        isPositive = True
        if str[0] == '-':
            isPositive = False
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        res = 0
        for ch in str:
            if not ch.isdigit():
                break
            res  = res * 10 + ord(ch) - ord('0')

        res = res if isPositive else -res
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN

        return res

if __name__ == "__main__":
    x = Solution()
    print x.myAtoi("34")
    print x.myAtoi("  34 ")
    print x.myAtoi("-34")
    print x.myAtoi("34a4")
    print x.myAtoi("a34")
    print x.myAtoi("3445689067890")
    print x.myAtoi("-")
    print x.myAtoi("4193 with words")
    print x.myAtoi("+34")
