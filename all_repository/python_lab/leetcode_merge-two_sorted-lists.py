# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """        
        new_list = ListNode()
        cur = new_list
    
        # Iterate for at most one list ended
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next                
                
        while list1 != None: # Not ended of list1
            cur.next = ListNode(list1.val)
            list1 = list1.next
            cur = cur.next
            
        while list2 != None: # Not ended of list2
            cur.next = ListNode(list2.val)
            list2 = list2.next
            cur = cur.next
            
        return new_list.next

if __name__ == "__main__":
    s = Solution()
    list1 = ListNode(1)
    list2 = ListNode(2)
    new_list = s.mergeTwoLists(list1, list2)
    new_list.print()