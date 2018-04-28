from heapq import heappush, heappop, heapify
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        heap = []
        freqMap = collections.Counter(tasks)
        taskObjs = []
        for task in freqMap.keys():
            taskObjs.append(Task(task, freqMap[task], 0))
        print freqMap
        #print taskObjs
        for task in taskObjs:
            heappush(heap, task)
        print heap
        pos = 0
        seq = ""
        while len(heap):
            print "Looking for task to assign at position " + str(pos)
            task = heappop(heap)
            if task.pos <= pos:
                print "Assigned task " + str(task)
                seq += task.task
                if task.count > 1:
                    task.count -= 1
                    task.pos = pos + n + 1
                    heappush(heap, task)
            else:
                seq += "_"
                heappush(heap, task)


            pos += 1
            print "Heap now" + str(heap)
        print "seq " + seq
        print " pos " + str(pos)



class Task(object):
    def __init__(self, task, count, pos):
        self.task = task
        self.count = count
        self.pos = pos
    def __cmp__(self, other):
        if self.pos != other.pos:
            return self.pos - other.pos
        else:
            return other.count - self.count
    def __repr__(self):
        s = ""
        s += "Task:" + self.task
        s += "||Count:" + str(self.count)
        s += "||Pos:" + str(self.pos)
        return s


if __name__ == "__main__":
    x = Solution()
    #x.leastInterval(["A","A","A","B","B","B"], 0)
    x.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)