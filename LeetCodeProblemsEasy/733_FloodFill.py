class Solution(object):
    def __init__(self, image):
        self.visited = []
        for i in range(len(image)):
            self.visited.append([])
            for j in range(len(image[0])):
                self.visited[i].append(0)
        print self.visited

    def isValidChild(self, image, x, y):
        maxRow = len(image)
        maxCol = len(image[0])
        return x < maxRow and x >= 0 and \
               y < maxCol and y >= 0

    def generateNeighbors(self, image, x, y):
        children = []
        for disp in [(0,-1), (0,1), (1,0), (-1,0)]:
            if self.isValidChild(image, x + disp[0], y + disp[1]):
                children.append((x + disp[0], y + disp[1]))
        #print "Children generated for " + str(x) + ":" + str(y) + " " + str(children)
        return children


    def floodFill(self, image, sr, sc, newColor):
        return self.floodFillHelper(image, sr, sc, newColor)

    def floodFillHelper(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        #print "Start processing " + str(sr) + ":" + str(sc)
        pixelColor = image[sr][sc]
        self.visited[sr][sc] = 1
        for nbr in self.generateNeighbors(image, sr, sc):
            nbrColor = image[nbr[0]][nbr[1]]
            if not self.visited[nbr[0]][nbr[1]] and pixelColor == nbrColor:
                self.floodFillHelper(image, nbr[0], nbr[1], newColor)
        image[sr][sc] = newColor
        return image
        #print "After processing " + str(sr) + ":" + str(sc) + "\n" + str(image)


if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    x = Solution(image)
    x.floodFill(image, sr, sc, newColor)


