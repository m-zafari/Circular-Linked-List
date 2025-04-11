# Mohammad Zafari
# mhdzafari80@gmail.com

class Node: 
       
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList: 
      
    def __init__(self): 
        self.head = None 
    
    def push(self, data): 
        given_node = Node(data) 
        temp = self.head 
          
        given_node.next = self.head 
   
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = given_node 
  
        else: 
            given_node.next = given_node 
  
        self.head = given_node 
         
    def count_nodes(self): 
        temp = self.head 
        if self.head is not None: 
            count = 0
            while(True): 
                count += 1 
                temp = temp.next
                if (temp == self.head): 
                    return count
        else:
            return 0
  
"""
list1 = CircularLinkedList()  
list1.push(12) 
list1.push(56) 
list1.push(2) 
list1.push(11)
list1.push(123)

# --> 123 --> 11 --> 2 --> 56 --> 12 -->
# ------<-------<-------<-------<-------

print(list1.count_nodes()) 
"""