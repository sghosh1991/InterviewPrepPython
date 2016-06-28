'''
Creation Date: Jun 27, 2016
@author : Santosh Ghosh

Problem Statement: A shoemaker has N orders from customers which he must satisfy. The shoemaker can work on only one job in each day, 
and jobs usually take several days. For the ith job, the integer Ti ( 1<=Ti<=1, 000) denotes the number of days it takes the shoemaker 
to finish the job.But popularity has its price. For each day of delay before starting to work on the ith job, the shoemaker has agreed 
to pay a fine of Si ( 1<=Si<=10, 000) cents per day. Help the shoemaker by writing a program to find the sequence of jobs with minimum 
total fine.

Input: Time array containing the time per task and Penalty array containing the penalty per day for not doing the work.

Output: An optiimal ordering of the tasks.

Logic Applied: http://www.algorithmist.com/index.php/UVa_10026. The approach that worked for me in this problem was the greedy approach. 
Basically we know that the higher the ratio of penalty to time, the earlier a job should be. Hence, we will sort our jobs based on this 
value and if two got the same ratio, we will sort based on position.
'''
import itertools

def minimum_penalty(time_required, penalty):
    
    index = itertools.count(1,1)
    penalty_to_day_ratio = [(-float(p)/t,i) for t,p,i in zip(time_required,penalty, index)]
    print penalty_to_day_ratio
    return sorted(penalty_to_day_ratio)


if __name__ == "__main__":
    
    time_required_per_job = [3,1,2,5]
    penalty_per_day = [4,1000,2,5]
    print minimum_penalty(time_required_per_job, penalty_per_day)