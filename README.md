# Circular-Linked-List
Push ---> add a node before self.head
count_nodes ---> count nodes in a circular linked list
# Example:
list1 = CircularLinkedList()  
list1.push(12) 
list1.push(56) 
list1.push(2) 
list1.push(11)
list1.push(123)

 --> 123 --> 11 --> 2 --> 56 --> 12 -->
 ------<-------<-------<-------<-------

print(list1.count_nodes()) 

output:
5
