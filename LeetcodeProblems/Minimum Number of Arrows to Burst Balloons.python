class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 1:
            return 0
        points = sorted(points, key= lambda x:(x[1],x[0]))
        #print points
        
        count = 1
        minEnd = points[0][1]
        
        for i in range (len(points)):
            if points[i][0] <= minEnd <= points[i][1]:
                pass
            else:
                count += 1
                minEnd =points[i][1]
          
        return count
            
        