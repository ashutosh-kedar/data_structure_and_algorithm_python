class Node:

    def __init__(self,value):
        self.value = value
        self.next = None




class LinkedList:

    def __init__(self):
        self.start = None


    def add(self,value):

        node = Node(value)

        if not self.start:
            self.start = node
            return

        itr_node = self.start
        while itr_node.next:
            itr_node = itr_node.next


        itr_node.next = node
        
        return

    def print_list(self):
        
        if not self.start:
            return ''
        item_list = ' '
        
        itr_node = self.start
        while itr_node:
            item_list += str(itr_node.value)+ '->'
            itr_node = itr_node.next

        return item_list


    def reverse_list(self):

        if not self.start:
            return

        current_node = self.start
        previous_node = None
        next_node = None


        while current_node:

            next_node = current_node.next
            current_node.next = previous_node
            
            previous_node = current_node
            current_node = next_node
            

        self.start = previous_node

        return



linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

print(f'LinkedList:{linked_list.print_list()}')

linked_list.reverse_list()

print(f'Reversed LinkedList:{linked_list.print_list()}')
        








                
        
