"""

"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        digits = map(lambda ch: int(ch), str(num))
        num_digits = len(digits)
        greatest_on_right = [(-1, -1)]*num_digits
        greatest_on_right[-1] = (-1, num_digits-1)
        max_on_right = (digits[-1], num_digits-1)
        for i in range(len(digits)-2, -1, -1):
            if max_on_right[0] < digits[i]:
                max_on_right = (digits[i], i)
            greatest_on_right[i] = max_on_right if digits[i] < max_on_right[0] else (-1, i)

        #print greatest_on_right
        for pos, greatest_on_right_digit in enumerate(greatest_on_right):
            if greatest_on_right_digit[0] != -1:
                (digits[pos], digits[greatest_on_right_digit[1]]) = (digits[greatest_on_right_digit[1]], digits[pos])
                break
        #print digits
        digits = "".join(map(lambda x: str(x), digits))
        return int(digits)

if __name__ == "__main__":
    x = Solution()
    #x.maximumSwap(2736)
    print x.maximumSwap(9973)
    print x.maximumSwap(12345)
    print x.maximumSwap(1)
    print x.maximumSwap(111)
