'''
Author: santosh
Creation Time: 2016:08:8/7/16

Problem Statement:Markov takes out his Snakes and Ladders game and stares at the board, and wonders: If he had absolute
control on the die (singular), and could get it to generate any number (in the range ) he desired, what would be the least
number of rolls of the die in which he'd be able to reach the destination square (Square Number ) after having started at the
base square (Square Number )?

Rules

Markov has total control over the die and the face which shows up every time he tosses it. You need to help him figure out the minimum number of moves in which he can reach the target square (100) after starting at the base (Square 1).

A die roll which would cause the player to land up at a square greater than 100, goes wasted, and the player remains at his original square. Such as a case when the player is at Square Number 99, rolls the die, and ends up with a 5.

If a person reaches a square which is the base of a ladder, (s)he has to climb up that ladder, and he cannot come down on it. If a person reaches a square which has the mouth of the snake, (s)he has to go down the snake and come out through the tail - there is no way to climb down a ladder or to go up through a snake.

Input:

Output:

Logic Applied:

Simple BFS style search. The children needs to be calculated with care. We neeed to take into account the
snake/ladder transitions also. the child of 1 can be 27 if there is a ladder from 3 to 27. Also we keep a visited
set to ensure that we donot visit an already visited nose as it will NEVER yield a shorter path => somebody before
has aleady visited this node.

'''
import sys

visited = set()
parent_child_mapping = dict()


def get_next_positions(curr_position, nexthop):
    """
    :param curr_position: the current position from which the directly reachable positions needs to be generated
    :param nexthop: the snakes and ladders transition table
    :return: a list of position which is directly reachable from the current position
    """
    global visited
    children = []
    print "Generating children for " + str(curr_position)
    for i in range(1, 7):

        if (curr_position + i) not in visited:
            if (curr_position + i) in next_hop:
                children.append(nexthop[curr_position + i])
                visited.add(nexthop[curr_position + i])
                visited.add(curr_position + i)
                parent_child_mapping[next_hop[curr_position + i]] = curr_position
            else:
                children.append(curr_position + i)
                visited.add(curr_position + i)
            parent_child_mapping[curr_position + i] = curr_position
    print children
    return children


def get_destination_to_source_path():

    global parent_child_mapping
    print "Generating the sequence"
    rolls_seq = list()
    parent = 100
    while parent != 1:
        rolls_seq.append((parent, parent_child_mapping[parent]))
        parent = parent_child_mapping[parent]
        print rolls_seq
    return rolls_seq


def get_minimum_die_rolls(nexthop):
    """
    :type nexthop: dictionary
    :param nexthop: A dictionary containing all the snake and ladder transitions
    :return: the minimum number of die rolls that is needed to reach the end
    """
    global visited, parent_child_mapping
    q = list()
    q.append(1)

    while len(q) != 0:
        curr_position = q[0]
        q = q[1:]
        next_reachable_positions = get_next_positions(curr_position, nexthop)
        if 100 in next_reachable_positions:
            sequence = get_destination_to_source_path()
            break
        q.extend(next_reachable_positions)

    min_number_of_die_rolls =  -1 if len(q)==0 else len(sequence)
    print min_number_of_die_rolls


if __name__ == "__main__":

    ip = sys.stdin
    global visited, parent_child_mapping

    num_test_cases = int(sys.stdin.readline().strip())

    for i in range(num_test_cases):

        # dictionary to keep the snakes as well as ladder positions
        next_hop = {}

        num_ladders = int(sys.stdin.readline().strip())

        for i in range(num_ladders):
            ladder_from_to = sys.stdin.readline().strip()
            next_hop[int(ladder_from_to.split()[0])] = int(ladder_from_to.split()[1])

        num_snakes = int(sys.stdin.readline().strip())

        for i in range(num_snakes):
            snake_from_to = sys.stdin.readline().strip()
            next_hop[int(snake_from_to.split()[0])] = int(snake_from_to.split()[1])

        print next_hop
        get_minimum_die_rolls(next_hop)
        visited = set()
        parent_child_mapping = dict()
