"""
Problem: Given mappings a=1, b=2....z=26. Given a string of numbers like 1123, you need to enumerate the various
string of alphabers possible from the integer string.
Example: 123 => abc (taking one digit at a time), lc(taking 12 together and then 3)

Solution: Recursive approach: strings possible from 123 => ( itoa(1) appended with strings possible from 23 )+
                                                           ( itoa(12) appended with strings possible from 3 )

Need to memoize as there are a lot of overlapping sub problems

"""

cache = {}

def itoa(i):
    return chr(int(i)+96)

def isValidEncoding(i):
    return int(i) <= 26


def generate_strings(encoded_string, spaces):

    #print "\t"*spaces + "called with " + encoded_string

    if encoded_string in cache:
        #print "\t"*spaces + "cache hit for " + encoded_string + " returning " + str(cache[encoded_string])
        return cache[encoded_string]

    # Base case 1: length of encoded_string = 0
    if len(encoded_string) == 0:
        #print "\t"*spaces + "base case length 0 hit"
        return ['']

    # Base case 2: length of encoded_string = 1
    if len(encoded_string) == 1:
        #print "\t"*spaces + "base case length 1 hit"
        cache[encoded_string[0]] = [itoa(encoded_string[0])]
        return [itoa(encoded_string[0])]

    # Recurse
    decoded_strings_1 = generate_strings(encoded_string[1:], spaces+1)
    decoded_strings_2 = generate_strings(encoded_string[2:], spaces+1)

    #print "\t"*spaces + "Returned 1 " + str(decoded_strings_1)
    #print "\t"*spaces + "Returned 2 " + str(decoded_strings_2)
    # Append
    res = []
    res1 = [itoa(encoded_string[0]) + str(y) for y in decoded_strings_1]
    res2 = [itoa(encoded_string[0:2]) + str(y) for y in decoded_strings_2] if isValidEncoding(encoded_string[0:2]) \
        else []

    res.extend(res1)
    res.extend(res2)

    cache[encoded_string] = res
    #print "\t"*spaces + str(cache)

    #print "\t"*spaces + "Returning combined " + str(res)
    return res

if __name__ == '__main__':

    res = generate_strings("1123", 0)
    print "Final res " + str(res)