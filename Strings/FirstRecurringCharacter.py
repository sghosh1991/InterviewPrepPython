"""

Find the first non-recurring character in a string

"""
import sys

def firstRecurringCharacter(s):
    if not s:
        return ''

    arr  = [ -1 for i in range(26)]
    for i, ch in enumerate(s):
        idx = ord(ch) - ord('a')
        if arr[idx] == -1:
            arr[idx] = i
        elif arr[idx] > -1:
            arr[idx] = -2
    # indices of elements occuring exactly once
    exactlyOnceIndices = [ idx for idx in arr if idx > -1]

    if len(exactlyOnceIndices) == 0:
        return ""
    return s[min(exactlyOnceIndices)]

if __name__ == "__main__":
    print "First non-recurring character is :" + str(firstRecurringCharacter("abca")) + ":"
    print "First non-recurring character is :" + str(firstRecurringCharacter("abc")) + ":"
    print "First non-recurring character is :" + str(firstRecurringCharacter("abbcac")) + ":"
    print "First non-recurring character is :" + str(firstRecurringCharacter("")) + ":"
