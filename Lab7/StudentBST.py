class BinaryTree():
    def __init__(self, students: list[dict]) -> None:
        root_id = students[0]['id']
        self.root = Node(root_id, students[0])
        for student in students[1:]:
            self.insert(student)
    
    def insert(self, student_data: dict):
        self.root.insert(student_data['id'], student_data)

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
            if val < node.psuid:
                node = node.left
            elif val > node.psuid:
                node = node.right
            elif val == node.psuid:
                return node

        return None
    
    def find_max(self):
        node: Node = self.root
        while node.right is not None:
            node = node.right

        return node.psuid 

    def find_min(self):
        node: Node = self.root
        while node.left is not None:
            node = node.left

        return node.psuid 

            

class Node:
    def __init__(self, psuid: int, student_data: dict = None, parent: 'Node' = None) -> None:
        self.psuid = psuid
        self.student_data = student_data
        self.parent = parent
        self.left: 'Node' = None
        self.right: 'Node' = None
    
    def in_order_traversal(self, temp: list):
        if self.left != None:
            self.left.in_order_traversal(temp)
        temp.append(self.student_data)
        if self.right != None:
            self.right.in_order_traversal(temp)

    def pre_order_traversal(self, temp: list):
        temp.append(self.student_data)
        if self.left != None:
            self.left.pre_order_traversal(temp)
        if self.right != None:
            self.right.pre_order_traversal(temp)

    def post_order_traversal(self, temp: list):
        if self.left != None:
            self.left.post_order_traversal(temp)
        if self.right != None:
            self.right.post_order_traversal(temp)
        temp.append(self.student_data)

    def insert(self, psuid: int, student_data: dict):
        if psuid <= self.psuid:
            if self.left != None:
                self.left.insert(psuid, student_data)
            else:
                self.left = Node(psuid, student_data, self)
        else:
            if self.right != None:
                self.right.insert(psuid, student_data)
            else:
                self.right = Node(psuid, student_data, self)

    def delete(self, val):
        if self.psuid > val:
            self.left.delete(val)
        elif self.psuid < val:
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
                    v = self.right.psuid
                else:
                    v = self._find_left_most_val()
                self.delete(v)
                self.psuid = v

    def _find_left_most_val(self):
        node = self.left
        while node.left is not None:
            node = node.left

        return node.psuid 


data_list = [
    {
        'id': 1,
        'name': 'James Charles',
        'email': 'jkc1231@psu.edu'
    },
    {
        'id': 2,
        'name': 'Amelia Watson',
        'email': 'awn412@psu.edu'
    },
    {
        'id': 3,
        'name': 'Michle Jakson',
        'email': 'mjn61@psu.edu'
    }
]

new_student = {
        'id': 4,
        'name': 'Jackie Welles',
        'email': 'jw94@psu.edu'
    }

tree = BinaryTree(data_list)
tree.insert(new_student)
print(f"{tree.find(1).student_data = }")
print()
for i in tree.in_order_traversal():
    print(i)