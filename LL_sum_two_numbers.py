# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#l1 = [2,4,3], l2 = [5,6,4]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
# https://takeuforward.org/data-structure/add-two-numbers-represented-as-linked-lists/

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    
    new_list_head = ListNode() 
    temp = new_list_head
    while (l1 or l2) or carry :
        sum_val = carry
        carry = 0
        if l1:
            sum_val += l1.val
            l1 = l1.next
            
        if l2:
            sum_val += l2.val
            l2 = l2.next
        
        if sum_val >= 10:
        #    print ("sum_val ", sum_val)
           carry = sum_val // 10
        #    print ("carry ", carry)
           sum_val = sum_val % 10
        # print ("sum_val ", sum_val)
           
        new_node = ListNode(sum_val)
        temp.next = new_node
        temp = new_node
    
    return new_list_head.next    
    
ptr = addTwoNumbers(l1, l2)

while ptr:
    print(ptr.val)
    ptr = ptr.next