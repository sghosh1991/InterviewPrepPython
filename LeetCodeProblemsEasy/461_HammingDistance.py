"""

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Hints: XOR followed by count set bits. Counting set bits can be done in many ways. Lookup table in O(1). Brutoforce O(n) Brian- Kerninghan Thets(n)

http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetTable
https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        differing_positions = x ^ y
        # Count set bits
        # c = 0
        # while(differing_positions):
        #     differing_positions &= differing_positions - 1
        #     c += 1
        # return c

        # Look up Table:
        c = 0
        bits_by_number = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        mask = 0xF
        shifter = 4
        for i in range(8):
            c += bits_by_number[differing_positions & mask]
            differing_positions = differing_positions >> shifter
        return c

if __name__ == '__main__':
    x = Solution()
    print x.hammingDistance(1577962638, 1727613287)

