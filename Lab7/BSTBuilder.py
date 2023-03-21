class BinaryTree():
    def __init__(self, items: list) -> None:
        self.root = Node(items[0])
        for i in items[1:]:
            self.root.insert(i)
            
    def insert(self, val: int):
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

def make_broken_tree():
    tree = BinaryTree([1, 7, 3, 8, 63, 188, 12, 731, 2, 998])
    # replace left node of the root tree to a bigger value 
    # thus resulting in a broken tree
    tree.root.left = Node(100, tree.root)
    return tree


def check_if_valid_tree(tree: BinaryTree):
    l = tree.in_order_traversal()
    last = l[0]
    # with a valid binary tree in order traversal will result in a sorted array, 
    # if the array isn't sorted then the tree is doing something wrong 
    for i in l:
        if i < last:
            return False
    return True

value_list = [9, 82, 16, 7, 21 ,9 ,43, 87, 125, 661]
working_tree = BinaryTree(value_list)
print(f"{working_tree.in_order_traversal() = }")

print(f"{check_if_valid_tree(working_tree) = }")
print(f"{check_if_valid_tree(make_broken_tree()) = }")
