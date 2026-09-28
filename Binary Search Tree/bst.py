from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None




class BST:

    def __init__(self):
        self.root = None



    def add(self,value):
        
        if not value:
            raise ValueError()

        node = Node(value)

        if not self.root:
            self.root = node
            return

        current_node = self.root

        while current_node:
            if current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    current_node.left = node
                    break
            elif current_node.value < value:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    current_node.right = node
                    break
        return

    def get_height(self,root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def print_bst_vertical(self):
        root = self.root
        
        if not root:
            return
        
        height = self.get_height(root)
        q = deque([(root, 0, (2**height))])  # node, level, spacing
        prev_level = 0
        line = ""
        
        while q:
            node, level, space = q.popleft()
            
            if level != prev_level:
                print(line)
                line = ""
                prev_level = level
            
            line += " " * (space // 2) + str(node.value) + " " * (space // 2)
            
            if node.left:
                q.append((node.left, level+1, space//2))
            if node.right:
                q.append((node.right, level+1, space//2))
        
        print(line)


if __name__ == '__main__':

    bst = BST()
    bst.add(5)
    bst.add(2)
    bst.add(7)
    bst.add(12)
    bst.add(6)
    bst.add(1)
    bst.add(3)
    bst.print_bst_vertical()

    #print(bst.root.right.right.value)
            
        
