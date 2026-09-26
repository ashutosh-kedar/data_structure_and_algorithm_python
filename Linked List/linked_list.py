class Node:
    def __init__(self,value):
        self.value = value
        self.next = None



class LinkedList:

    def __init__(self):
        self.start = None

    def add(self,value):
        node = Node(value)
        node.value = value
        
        if not self.start:
            self.start = node
            return None

        itr_node = self.start
        while(itr_node.next):
            itr_node = itr_node.next

        itr_node.next = node

        return None

    def get_list(self):
        
        if not self.start:
            return '[]'
        values = '['
        itr_node = self.start
        while itr_node:
            values = values + str(itr_node.value) + ','
            itr_node = itr_node.next

        values = values + ']'

        return values

    def reverse_list(self):

        if not self.start:
            return None


        current_node = self.start
        next_node = None
        prev_node = None

        while current_node:

            next_node = current_node.next
            current_node.next = prev_node
            
            if not next_node:
                self.start = current_node

            prev_node = current_node
            current_node = next_node

        

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
print(f'List:{linked_list.get_list()}')  
linked_list.reverse_list()
print(f'Reveresed List:{linked_list.get_list()}')        
        
        
