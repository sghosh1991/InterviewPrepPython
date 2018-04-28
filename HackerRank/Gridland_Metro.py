'''
https://www.hackerrank.com/challenges/gridland-metro/problem
'''

import sys
from collections import defaultdict, deque
from operator import itemgetter, attrgetter, methodcaller

def gridlandMetro(n, m, k, track):
    track_by_row = defaultdict(list)
    for rail_track in track:
        track_by_row[rail_track[0] - 1].append((rail_track[1] - 1, rail_track[2] - 1))

    #print str(track_by_row)
    occupied_cells = 0
    for row in track_by_row.keys():
        merged_intervals = merge_intervals(track_by_row[row])
        for interval in merged_intervals:
            occupied_cells += interval[1] - interval[0] + 1

    #print " Number of lamposts " +  str(n*m - occupied_cells)
    return n*m - occupied_cells


def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=itemgetter(0))
    #print 'Sorted intervals ' + str(sorted_intervals)
    res_intervals = []
    if(len(sorted_intervals) == 0):
        return []
    merged_intervals = deque()
    merged_intervals.appendleft(sorted_intervals[0])
    merged_intervals_count = 1
    for idx in range(1, len(intervals)):
        temp_interval = merged_intervals.popleft()
        merged_intervals_count -= 1
        if overlaps(temp_interval, sorted_intervals[idx]):
            #print "Overlap " + str(temp_interval) + " " + str(sorted_intervals[idx])
            union_of_interval = (min(temp_interval[0], intervals[idx][0]), max(temp_interval[1], intervals[idx][1]))
            merged_intervals.appendleft(union_of_interval)
            merged_intervals_count += 1
        else:
            #print "No overlap " + str(temp_interval) + " " + str(sorted_intervals[idx])
            res_intervals.append(temp_interval)
            res_intervals.append(intervals[idx])

        idx += 1
    if merged_intervals_count == 1:
        res_intervals.append(merged_intervals.popleft())
    #print "Merged intervals" + str(res_intervals)
    return res_intervals


def overlaps(interval1, interval2):
    return not (interval1[1] < interval2[0] or interval2[1] < interval1[0])


if __name__ == "__main__":
    # n, m, k = raw_input().strip().split(' ')
    # n, m, k = [int(n), int(m), int(k)]
    # track = []
    # for track_i in xrange(k):
    #     track_temp = map(int,raw_input().strip().split(' '))
    #     track.append(track_temp)
    n = 4
    m = 4
    k = 3

    track = [
        [2, 2, 3],
        [2, 1, 3],
        [4, 4, 4]
    ]
    result = gridlandMetro(n, m, k, track)
    print result