'''
NOT DONE YET
'''

from operator import itemgetter
def keyFunc(numpos):
    return numpos[1]*numpos[0]

def cmpFunc(numpos1, numpos2):
    (num1, idx1) = numpos1
    (num2, idx2) = numpos2
    print " Comparing " + str(numpos1) + " " + str(numpos2)

    p = 0
    if(num1 > num2):
        p = idx2 - idx1
    elif(num1 < num2):
        p = idx1 - idx2
    else:
        p = idx1 - idx2
    print p
    return p



class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        digitsAndPos = [(int(x),len(num)-i) for (i,x) in enumerate(num)]
        print digitsAndPos
        # sortByDigitsDesc = sorted(digitsAndPos, key=itemgetter(0), reverse=True)
        # print sortByDigitsDesc
        # sortByAscPos = sorted(sortByDigitsDesc, key=itemgetter(1))
        # print sortByAscPos
        # p = ''.join([ x[0] for x in sortByAscPos[k:]])
        # print p
        # return p
        arr = sorted(digitsAndPos, key=keyFunc)
        print arr



if __name__ == "__main__":
    x = Solution()
    x.removeKdigits("1432219", 3)