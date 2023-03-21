class BinaryTree():
    def __init__(self, items: list) -> None:
        self.items = items
        self.root: Node
        self._create_tree()
        
    def _create_tree(self):
        self.root = Node(self.items[0])
        for i in self.items[1:]:
            self.root.insert(i)

    def insert(self, val: int):
        self.items.append(val)
        self.root.insert(val)

    def in_order_traversal(self):
        temp = []
        self.root.in_order_traversal(temp)
        return temp

    def pre_order_traversal(self):
        temp = []
        self.root.pre_order_traversal(temp)
        return temp

    def post_order_traversal(self):
        temp = []
        self.root.post_order_traversal(temp)
        return temp

    def delete(self, val):
        self.root.delete(val)

    def find(self, val):
        node: Node = self.root
        while node != None:
            if val < node.data:
                node = node.left
            elif val > node.data:
                node = node.right
            elif val == node.data:
                return node

        return None
    
    def find_max(self):
        node: Node = self.root
        while node.right is not None:
            node = node.right

        return node.data 

    def find_min(self):
        node: Node = self.root
        while node.left is not None:
            node = node.left

        return node.data 

            

class Node:
    def __init__(self, data: int, parent: 'Node' = None) -> None:
        self.data = data
        self.parent = parent
        self.left: 'Node' = None
        self.right: 'Node' = None
    
    def in_order_traversal(self, temp: list):
        if self.left != None:
            self.left.in_order_traversal(temp)
        temp.append(self.data)
        if self.right != None:
            self.right.in_order_traversal(temp)

    def pre_order_traversal(self, temp: list):
        temp.append(self.data)
        if self.left != None:
            self.left.pre_order_traversal(temp)
        if self.right != None:
            self.right.pre_order_traversal(temp)

    def post_order_traversal(self, temp: list):
        if self.left != None:
            self.left.post_order_traversal(temp)
        if self.right != None:
            self.right.post_order_traversal(temp)
        temp.append(self.data)

    def insert(self, data: int):
        if data <= self.data:
            if self.left != None:
                self.left.insert(data)
            else:
                self.left = Node(data, self)
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = Node(data, self)

    def delete(self, val):
        if self.data > val:
            self.left.delete(val)
        elif self.data < val:
            self.right.delete(val)
        else:
            # Case where self is a leaf node
            if self.left is None and self.right is None:
                if self.parent.left is self:
                    self.parent.left = None
                elif self.parent.right is self:
                    self.parent.right = None
            # Case where self is a single line
            elif self.left is None:
                if self.parent.left is self:
                    self.right.parent = self.parent
                    self.parent.left = self.right
                elif self.parent.right is self:
                    self.right.parent = self.parent
                    self.parent.right = self.right
            elif self.right is None:
                if self.parent.left is self:
                    self.left.parent = self.parent
                    self.parent.left = self.left
                elif self.parent.right is self:
                    self.left.parent = self.parent
                    self.parent.right = self.left
            # Case where self have both left and right node
            else:
                if self.parent is None:
                    v = self.right.data
                else:
                    v = self._find_left_most_val()
                self.delete(v)
                self.data = v

    def _find_left_most_val(self):
        node = self.left
        while node.left is not None:
            node = node.left

        return node.data 

def tree_merger(tree1: BinaryTree, tree2: BinaryTree):
    t1 = tree1.pre_order_traversal()
    t2 = tree2.pre_order_traversal()
    t1.extend(t2)
    temp = BinaryTree(t1)
    return temp

t = BinaryTree([5, 1, 4, 6, 2, 3, 8, 7, 9, 0])
t.insert(11)
print(f"{t.in_order_traversal() = }")
print(f"{t.pre_order_traversal() = }")
print(f"{t.post_order_traversal() = }")
n = t.find(5)
print(f"{n.data = }")
print(f"{t.find_min() = }")
print(f"{t.find_max() = }")
t.delete(0)
print(f"{t.in_order_traversal() = }")
t.delete(2)
print(f"{t.in_order_traversal() = }")
t.delete(8)
print(f"{t.in_order_traversal() = }")

t1 = BinaryTree([8, 12, 42, 77, 13, 88, 91, 9, 44, 87])
t2 = BinaryTree([2, 24, 5, 64, 32, 13, 56, 71, 51, 77])
merged = tree_merger(t1, t2)
print(f"{merged.in_order_traversal() = }")