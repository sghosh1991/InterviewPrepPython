'''
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = {}
        idx = 0
        stackLen = 0
        while idx < len(temperatures):
            print "Inspecting element " + str(temperatures[idx]) + " at index " + str(idx)
            # Push on stack
            if(stackLen and temperatures[idx] < stack[-1][0]):
                stack.append((temperatures[idx], idx))
                stackLen += 1
                idx += 1
                print "StackLen " + str(stackLen) + " Stack "  + str(stack)
                print "Res " + str(res)
                continue
            else:
                temp = temperatures[idx]
                while(stackLen and temp > stack[-1][0]):
                    (nextWaremerDatFor, pos) = stack.pop()
                    res[(nextWaremerDatFor, pos)] = idx - pos
                    stackLen -= 1
            stack.append((temperatures[idx], idx))
            stackLen += 1
            idx += 1
            print "StackLen " + str(stackLen) + " Stack "  + str(stack)
            print "Res " + str(res)
        for elem in stack:
            res[elem] = 0
        print "Res " + str(res)

        return [ res[(temp,pos)] for pos,temp in enumerate(temperatures)]

if __name__ == "__main__":
    x = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print x.dailyTemperatures(temperatures)
