# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None and l2 == None:
            return None
        
        the_map = [-101] * 201
        
        while(l1 != None):
            #print("inside loop for l1")
            the_map[l1.val + 100] += 1
            l1 = l1.next
            
        while(l2 != None):
            the_map[l2.val + 100] += 1
            l2 = l2.next
        
        output = []
        
        for i in range (len(the_map)):
            if(the_map[i] != -101):
                #print("inside if to put value in output")
                #for j in range(101 + )
                output.extend([i - 100] * (the_map[i] + 101))
                #print("done putting value in output")
                #print(output)
                
        #print(output)
        
        
        
        current_node = ListNode()
        temp = current_node
        
        for i in range(len(output)):
            current_node.val = output[i]
            if(i + 1 != len(output)):
                #print("indised for", current_node.val)
                new_node = ListNode()
                current_node.next = new_node
                current_node = new_node
        
        #print("printing outside the final for", current_node.val)
        
        return temp
            
        
        
        
