"""

*** INCOMPLETE ****


"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Asuume 3 or more elements.
        # handle otherwise cases
        #print "*"*10 + "\n"

        numPrices = len(prices)
        if numPrices <= 1:
            return 0
        i = 1
        maxProfit = 0
        while True:
            #print "Starting search for increasing subarray at " + str(i)
            madeTransaction = False
            while i < numPrices and prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
                i += 1
                madeTransaction = True
             #   print "Increasing subarray anding at " + str(i) + " profit till now " + str(maxProfit)

            #print "Non increasing price or end of prices. Ended loop at " + str(i)
            if i < numPrices and madeTransaction:
                #print "Transaction was made entering cooloff....."
                i += 2
                continue
            if i >= numPrices:
                break
            i += 1
            #print "While loop end..Looping over"
        return maxProfit

if __name__ == "__main__":
    x = Solution()
    print x.maxProfit([8,2,6,7,5,4,3,11,13,8,7])
    print x.maxProfit([5,4,3,2,1])
    print x.maxProfit([1,2,3,4,5,6])




