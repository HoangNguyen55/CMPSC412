from random import randint
from collections import deque

class BinaryTreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_key=None):
        # maps from BinaryTreeNode key to BinaryTreeNode instance.
        # Thus, BinaryTreeNode keys must be unique.
        self.nodes = {}
        if root_key is not None:
            # create a root BinaryTreeNode
            self.root = BinaryTreeNode(root_key)
            self.nodes[root_key] = self.root

    def add(self, key, left_key=None, right_key=None):
        if key not in self.nodes:
            # BinaryTreeNode with given key does not exist, create it
            self.nodes[key] = BinaryTreeNode(key)
        # invariant: self.nodes[key] exists

        # handle left child
        if left_key is None:
            self.nodes[key].left = None
        else:
            if left_key not in self.nodes:
                self.nodes[left_key] = BinaryTreeNode(left_key)
            # invariant: self.nodes[left_key] exists
            self.nodes[key].left = self.nodes[left_key]

        # handle right child
        if right_key == None:
            self.nodes[key].right = None
        else:
            if right_key not in self.nodes:
                self.nodes[right_key] = BinaryTreeNode(right_key)
            # invariant: self.nodes[right_key] exists
            self.nodes[key].right = self.nodes[right_key]

    def remove(self, key):
        if key not in self.nodes:
            raise ValueError('%s not in tree' % key)
        # remove key from the list of nodes
        del self.nodes[key]
        # if node removed is left/right child, update parent node
        for k in self.nodes:
            if self.nodes[k].left and self.nodes[k].left.key == key:
                self.nodes[k].left = None
            if self.nodes[k].right and self.nodes[k].right.key == key:
                self.nodes[k].right = None
        return True

    def _height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def height(self):
        return self._height(self.root)

    def size(self):
        return len(self.nodes)

    def __repr__(self):
        return str(self.traverse_inorder(self.root))

    def bfs(self, node):
        if not node or node not in self.nodes:
            return
        reachable = []    
        q = deque()
        # add starting node to queue
        q.append(node)
        while len(q):
            visit = q.popleft()
            # add currently visited BinaryTreeNode to list
            reachable.append(visit)
            # add left/right children as needed
            if visit.left:
                q.append(visit.left)
            if visit.right:
                q.append(visit.right)
        return reachable

    # visit left child, root, then right child
    def traverse_inorder(self, node, reachable=None):
        if not node or node.key not in self.nodes:
            return
        if reachable is None:
            reachable = []
        self.traverse_inorder(node.left, reachable)
        reachable.append(node.key)
        self.traverse_inorder(node.right, reachable)
        return reachable

    # visit left and right children, then root
    # root of tree is always last to be visited
    def traverse_postorder(self, node, reachable=None):
        if not node or node.key not in self.nodes:
            return
        if reachable is None:
            reachable = []
        self.traverse_postorder(node.left, reachable)
        self.traverse_postorder(node.right, reachable)
        reachable.append(node.key)
        return reachable

    # visit root, left, then right children
    # root is always visited first
    def traverse_preorder(self, node, reachable=None):
        if not node or node.key not in self.nodes:
            return
        if reachable is None:
            reachable = []
        reachable.append(node.key)
        self.traverse_preorder(node.left, reachable)
        self.traverse_preorder(node.right, reachable)
        return reachable       


class BinarySearchTree():
    def __init__(self, root: int) -> None:
        self.root = BSTNode(root)
        
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
        node: BSTNode = self.root
        while node != None:
            if val < node.data:
                node = node.left
            elif val > node.data:
                node = node.right
            elif val == node.data:
                return node

        return None
    
    def find_max(self):
        node: BSTNode = self.root
        while node.right is not None:
            node = node.right

        return node.data 

    def find_min(self):
        node: BSTNode = self.root
        while node.left is not None:
            node = node.left

        return node.data 

class BSTNode:
    def __init__(self, data: int, parent: 'BSTNode' = None) -> None:
        self.data = data
        self.parent = parent
        self.left: 'BSTNode' = None
        self.right: 'BSTNode' = None
    
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
                self.left = BSTNode(data, self)
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = BSTNode(data, self)

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

class SinglyNode():
    def __init__(self, data, next_node:'SinglyNode' = None) -> None:
        self.data = data
        self.next_node = next_node

class SinglyList(SinglyNode):
    def __init__(self, data) -> None:
        super().__init__(data)
    
    def MiddleInsert(self, index, value):
        new = SinglyNode(value)
        node = self
        # traverse the list to the target index
        for _ in range(0, index-1):
            node = node.next_node

        # point the new node to the node that the target index pointed to
        new.next_node = node.next_node
        # point the current node's next to the new node
        node.next_node = new

    def StartInsert(self, value):
        # create a new node and point that new node's next to the current next
        new = SinglyNode(value, self.next_node)

        # replace current next to the new node
        self.next_node = new

    def EndInsert(self, value):
        new = SinglyNode(value)
        node = self
        # traverse until the end
        while node.next_node:
            node = node.next_node
        
        # add new node as the end node's next
        node.next_node = new

    def Delete(self, index):
        node = self
        # go to target index minus 1
        for _ in range(0, index-1):
            node = node.next_node

        # replace the current node's next node to the actual target index's next node
        # which will effectively remove the targeted index node
        node.next_node = node.next_node.next_node

    def Traverse(self):
        # go through each node and print it's data
        node = self
        while node.next_node:
            print(str(node.data) + " -> ", end="")
            node = node.next_node

        # print the final node as the loop won't print it    
        print(node.data)

    def Reverse(self):
        # list use to store data of every single nodes
        all_nodes = []
        node = self
        # go through each node and store its data
        while node.next_node:
            all_nodes.append(node.data)
            node = node.next_node
        all_nodes.append(node.data)

        # iterate through all value of all_nodes in reverse and update
        # the value of the nodes
        node = self
        for _ in range(0, len(all_nodes)):
            node.data = all_nodes.pop()
            node = node.next_node

l = []
d = {}
bst = BinarySearchTree(0)
ll = SinglyList(0)