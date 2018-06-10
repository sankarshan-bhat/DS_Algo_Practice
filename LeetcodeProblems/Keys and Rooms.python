class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) < 1:
            return False
        Visitedarry = [False]*len(rooms)
        
        keysQueue = []
        keysQueue.append(rooms[0])
        Visitedarry[0] = True
        while len(keysQueue) > 0:
            #print "keysQueue" ,keysQueue
            keys = keysQueue.pop(0)
            if type(keys) == int:
                keys = [keys]
            #print "keys", keys
            for i in range(len(keys)):
                Visitedarry[keys[i]] = True
                tempArry = rooms[keys[i]]
                if type(tempArry) == int:
                    tempArry = [tempArry]
                #print "len(tempArry)",len(tempArry)
                #print "tempArry",tempArry
                for i in range (len(tempArry)):
                    if not (Visitedarry[tempArry[i]]):
                        keysQueue.append(tempArry[i])
                #print "keysQueue" ,keysQueue
        print Visitedarry 
        
        for i in range(0,len(Visitedarry)):
            if not (Visitedarry[i]):
                return False
            
        return True
        
        
                
        