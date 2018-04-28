'''
https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
'''

#!/bin/python

import sys

def overlaps(interval1, interval2):
    #print "Comparing intervals  " + str(interval1) + " " + str(interval2)
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return False
    return True

def hackerlandRadioTransmitters(x, k):
    # Complete this function
    covered_intervals = []
    sorted_house_pos = sorted(x)
    print " Sorted arraay " + str(x) + "\n\n"
    for house_pos in sorted_house_pos:
        covering_interval = (house_pos - k, house_pos + k, house_pos)
        #print "Checking house pos " + str(house_pos) + " " + str(covering_interval)
        if len(covered_intervals) > 0:
            if not overlaps(covered_intervals[len(covered_intervals)-1], covering_interval):
                #print " Adding an interval " + str(covering_interval)
                covered_intervals.append(covering_interval)
            else:
                pass
                #print "Donot add " + str(covering_interval)
        else:
            #print "Adding an interval " + str(covering_interval)
            covered_intervals.append(covering_interval)
    print "Current intervals " +  str(covered_intervals) + "\n\n\n"

    last_pos = sorted_house_pos[len(sorted_house_pos)-1]
    last_covered_interval = covered_intervals[len(covered_intervals) -1]

    if last_covered_interval[1] + k == last_pos:
        covered_intervals.append(last_pos-k, last_pos + k)

    print "Current intervals " +  str(covered_intervals) + "\n"
    return len(covered_intervals)





if __name__ == "__main__":
    # n, k = raw_input().strip().split(' ')
    # n, k = [int(n), int(k)]
    # x = map(int, raw_input().strip().split(' '))
    k = 2
    x = [0,6]

    result = hackerlandRadioTransmitters(x, k)
    print result
