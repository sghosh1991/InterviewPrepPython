"""
Author: santosh
Creation Time: 2016:08:8/8/16

Problem Statement: https://www.hackerrank.com/challenges/red-john-is-back

Input:

Output:

Logic Applied: Very convoluted logic!!

Say N = 10. Then max number of 1X4 possible = 2. Now we have 10 - 2*4 = 2 places left. After placing 2 1X4 tiles,
we have to place two 4X1 tiles. there are 3 locations where we can place the 2 4X1 tiles => one between the two 1X4 tiles
and the at either end. No the problem is like this => we have 3 types of positions as mentioned above and we need to select
2 positions out of these 3 with possible repetations.

The formula (i had to google it up!!) is here : http://www.math.northwestern.edu/~mlerma/courses/cs310-05s/notes/dm-gcomb

 IDEA: To build a 4XN wall i need to stack up 4 1X4 blocks. So knowing how can we place one of these 1X4 is enough.

"""
import sys


T = list()


def print_matrix():
    global T
    #print "***************************"
    for row in T:
        print row


def create_combination_table(N):
    for i in range(N + 1):
        row = [0] * (N + 1)
        T.append(row)

    # printMatrix()
    #print "After init"

    for i in range(N + 1):
        T[0][i] = 1
        T[i][i] = 1
        # printMatrix()

    for r in range(1, N + 1):
        for n in range(r + 1, N + 1):
            T[r][n] = T[r][n - 1] + T[r - 1][n - 1]

    #print_matrix()


def find_number_of_ways_to_build_wall(N):

    create_combination_table(N)

    max_num_1X4_possible = N / 4
    combinations = 0
    for i in range(max_num_1X4_possible, 0, -1):
        #print "Finding combinations with " + str(i) + " 1X4 " + "tiles placed"
        possible_slots = i + 1
        remaining_slots = N - i * 4
        combinations += T[remaining_slots][remaining_slots + possible_slots - 1]
        #print " Combinations of this type possible " + str(T[remaining_slots][remaining_slots + possible_slots - 1])
        #print " Cumulative combination " + str(combinations)

    return combinations+1


def sieve_of_eratosthenes(N):
    l = range(2, N + 1)
    s = set(l)

    for i in l:

        if i not in s:
            continue
        else:
            p = 2
            while i * p <= N:
                if i * p in s:
                    s.remove(i * p)
                p += 1
    print len(s)

if __name__ == "__main__":

    #global T
    num_test_cases = int(sys.stdin.readline().strip())
    for i in range(num_test_cases):
        N = int(sys.stdin.readline().strip())

        n = find_number_of_ways_to_build_wall(N)
        sieve_of_eratosthenes(n)
        T = list()
