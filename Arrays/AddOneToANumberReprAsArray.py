"""

Given a number represented as an array add one to it and resturn another array that
represents the incremented number

"""

def incr(num):
    numLength = len(num)

    carry = 1
    i = numLength-1
    while i >= 0:
        if num[i] + carry == 10:
            num[i] = 0
            i -= 1
        else:
            num[i] += carry
            return num
    res = [1]
    res.extend(num)
    return res

if __name__ == "__main__":
    print str(incr([1,2,3,4]))
    print str(incr([1,2,9,9]))
    print str(incr([4]))
    print str(incr([9]))
    print str(incr([9,9,9]))


