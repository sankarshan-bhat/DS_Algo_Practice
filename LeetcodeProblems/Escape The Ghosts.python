class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        target_dis = abs(target[0]-0)+ abs(target[1]-0)
        
        for gDisvh, gDisv in ghosts:
            ghosy_dis = abs(gDisvh-target[0]) +  abs(gDisv-target[1])
            
            if ghosy_dis <= target_dis:
                return False
        return True