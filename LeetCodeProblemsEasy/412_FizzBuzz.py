'''



'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return map(self.itofizzbuzz, range(1,n+1))

    def itofizzbuzz(self, x):
        if x % 15 == 0:
            return "FizzBuzz"
        elif x % 3 == 0:
            return "Fizz"
        elif x % 5 == 0:
            return "Buzz"
        else:
            return str(x)

if __name__ == '__main__':
    x = Solution()
    print x.fizzBuzz(15)