"""
https://leetcode.com/problems/course-schedule-ii/description/
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.discovered = set()
        self.processed = set()
        self.topo_order = []
        self.cycle_present = 0

        self.prerequisites_adj_list = [ [] for i in range(numCourses) ]
        for [course, prereq_course] in prerequisites:
            self.prerequisites_adj_list[prereq_course].append(course)

        print self.prerequisites_adj_list

        for i in range(numCourses):
            if i not in self.discovered:
                self.dfs(i)
        if self.cycle_present:
            self.topo_order = []
        else:
            self.topo_order = self.topo_order[::-1]
        return self.topo_order



    def dfs(self, node):

        self.discovered.add(node)
        for neighbor in self.prerequisites_adj_list[node]:
            if neighbor in self.processed:
                continue
            if neighbor in self.discovered:
                self.cycle_present = 1
            else:
                self.dfs(neighbor)
        self.processed.add(node)
        self.topo_order.append(node)


if __name__ == "__main__":
    x = Solution()
    print x.findOrder(4, [[1,0],[2,0],[3,1],[3,2]] )
    print x.findOrder(2, [[0,1]])
    print x.findOrder(2, [[0,1], [1,0]])