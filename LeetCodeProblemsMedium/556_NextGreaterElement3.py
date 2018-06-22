"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Logic: Traverse from R to L. If all of the r->L digits are in ascending order then return -1
Else find the first inversion, i.e a location where a[i-1] > a[i]
We need to switch a[i-1] with a[i]. This makes the next greater number. Now the question is where to place the a[i-1]th number such that it is just
greater than the original number. So we need to find the nu,ber that is just smaller than a[i-1].
We can do so by putting on a stack all the numbers so far uptill the inversion.
Then keep on popping from the stack till we get a number smaller than a[i-1]. We switch them. Note that all numbers in stack are inascending order

"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = []
        nstr = str(n)
        i = len(nstr)-1
        while i >= 0:
            stack.append(nstr[i])
            if nstr[i-1] < nstr[i]:
                break
            i -= 1

        if i == -1:
            return i
        else:
            print "stack " + str(stack)
            result = list(nstr[:i]) # Partial result
            # Inversion
            inversionElem = nstr[i-1]
            temp = [inversionElem]
            print "temp " + str(temp)
            print "stack " + str(stack)
            greatestElementSmallerThanInversionElem = stack.pop()
            while len(stack) and inversionElem <= greatestElementSmallerThanInversionElem:
                temp.append(greatestElementSmallerThanInversionElem)
                greatestElementSmallerThanInversionElem = stack.pop()
                print "temp " + str(temp)
                print "stack " + str(stack)
            if(len(stack)):
                temp.extend(stack)
            print "temp " + str(temp)
            result.append(greatestElementSmallerThanInversionElem)
            result.extend(sorted(temp))

        return "".join(result)

if __name__ == "__main__":
    x = Solution()
    print x.nextGreaterElement(6743)




