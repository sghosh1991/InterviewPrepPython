'''
NOT DONE YET
'''
import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #distMap = collections.defaultdict(set)
        distMap = {}
        res = 0
        for i in range(len(points)-1):
            for j in (range(i+1, len(points))):
                print "inspecting " + str(points[i]) + " and " + str(points[j])
                dist_i_j = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                if((points[i][0],points[i][1]) in distMap):
                    if( dist_i_j in distMap[(points[i][0],points[i][1])] ):
                        distMap[(points[i][0],points[i][1])][dist_i_j].add((points[j][0], points[j][1]))
                    else:
                        distMap[(points[i][0],points[i][1])][dist_i_j] = { (points[j][0], points[j][1]) }
                else:
                    distMap[(points[i][0],points[i][1])] = { dist_i_j : { (points[j][0], points[j][1]) } }

                if((points[j][0],points[j][1]) in distMap):
                    if( dist_i_j in distMap[(points[j][0],points[j][1])] ):
                        distMap[(points[j][0],points[j][1])][dist_i_j].add((points[i][0], points[i][1]))
                    else:
                        distMap[(points[j][0],points[j][1])][dist_i_j] = { (points[i][0], points[i][1]) }
                else:
                    distMap[(points[j][0],points[j][1])] = { dist_i_j : { (points[i][0], points[i][1]) } }

        print distMap



if __name__ == "__main__":
    x = Solution()
    arr = [[0,0],[1,0],[2,0]]
    x.numberOfBoomerangs(arr)