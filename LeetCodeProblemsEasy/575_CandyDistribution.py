'''

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.


'''

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        sister_candies = set()
        num_candies = len(candies)
        for candy in candies:
            if candy not in sister_candies:
                sister_candies.add(candy)
                if len(sister_candies) == num_candies / 2:
                    break
        return len(sister_candies)
        # More elegant solution. Ideas was similar. Max num of candy types the sister can have = num candoes / 2
        # so min is needed if candy types are more than num candies /2.
        # return min(len(set(candies)), len(candies)/2)


