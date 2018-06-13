# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumNode = dummy=ListNode(0)
        c = 0
        while ( l1  or l2 or c ==1):
            
            a1,l1 = (l1.val,l1.next) if l1 else (0,None)
            a2,l2 = (l2.val,l2.next) if l2 else (0,None)
            c,s = divmod(a1+a2+c,10)
            print s,c
           
            sumNode.next = ListNode(s)
            sumNode = sumNode.next
    
            
        return dummy.next
            
        
                
                
        