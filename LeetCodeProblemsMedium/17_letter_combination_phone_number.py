"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""
class Solution(object):

    def __init__(self):
        self.results = []
        self.mappings = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        self.num_digits = 0


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = digits
        self.num_digits = len(digits)
        self.combinations_helper(["" for i in range(self.num_digits)], 0)
        return self.results

    def combinations_helper(self, partial_res, position):
        if position == self.num_digits:
            self.results.append("".join(partial_res))
        else:
            for ch in self.mappings[int(self.digits[position])]:
                partial_res[position] = ch
                self.combinations_helper(partial_res, position + 1)

if __name__ == "__main__":
    x = Solution()
    print x.letterCombinations("23")
