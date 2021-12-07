
class BST:
    class Node:
        def __init__(self, data):
            self.data = data # Data of the node
            self.left = None # Data to the left of the node
            self.right = None # Data to the right of the node
    
    def __init__(self):
        self.root = None # Defining the root node

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        
        if data == node.data: # Data Already Existant
            return
        elif data['id'] < node.data['id']: # Number is less than the data
            if node.left is None: # No data found, insert it in the left
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None: # Number is greater than the data
                node.right = BST.Node(data) # No data found, insert in right
            else:
                self._insert(data, node.right)

    def find(self, id):
        if id == self.root.data['id']: # Name is the root
            print(self.root.data['f_name'])
        else:
            self._find(id, self.root)
    
    def _find(self, id, node):
        if node.data == None or node.data == None:
            print("USER NOT FOUND")
        else:
            if id == node.data['id']: # Name Found
                print(node.data['f_name'])
            elif id > node.data['id']: # ID greater than node, check right
                self._find(id, node.right)
            else: # ID less than node, check left
                self._find(id, node.left)

    def find_all(self):
        if self.root.left == None and self.root.right == None:
            print(self.root.data['f_name'])
        else:
            self._find_all(self.root)

    def _find_all(self, node):
        if node == None:
            return
        elif node.left != None:
            self._find_all(node.left)
        elif node.right != None:
            self._find_all(node.right)
        print(node.data['f_name'])

    def remove(self, id):
        if id == self.root.data['id']:
            self.root = None
        else:
            self._remove(id, self.root)

    def _remove(self, id, node):
        if id == node.data['id']: # Name Found
            print(f"REMOVING {node.data['f_name']}")
            node.data = None
        elif id > node.data['id']: # ID Greater than node, check right
            self._remove(id, node.right)
        else:
            self._remove(id, node.left)

root = BST()

database = [
    {'id': 4, 'f_name': 'John',  'l_name': 'Feltze',   'age': 32, 'eye_color': 'Hazel',      'hair_color': 'Blonde'},
    {'id': 2, 'f_name': 'Sandy', 'l_name': 'Cheeks',   'age': 22, 'eye_color': 'Brown',      'hair_color': 'Brown'},
    {'id': 6, 'f_name': 'Peter', 'l_name': 'Clark',    'age': 19, 'eye_color': 'Blue',       'hair_color': 'Blonde'},
    {'id': 1, 'f_name': 'Blake', 'l_name': 'Stofferd', 'age': 48, 'eye_color': 'Blue',       'hair_color': 'Red'},
    {'id': 3, 'f_name': 'Randy', 'l_name': 'Ratchet',  'age': 75, 'eye_color': 'Greeb',      'hair_color': 'White'},
    {'id': 5, 'f_name': 'Mary',  'l_name': 'Krinkle',  'age': 53, 'eye_color': 'Brown',      'hair_color': 'Brown'},
    {'id': 7, 'f_name': 'Lucy',  'l_name': 'Phillips', 'age': 41, 'eye_color': 'Blue-Green', 'hair_color': 'Blonde'}
]

# INSERTING EACH PERSON INTO THE TREE
for person in database:
    root.insert(person)

# FINDING A PERSON IN THE TREE
print("FINDING USERS. . .")
root.find(5) # Mary
root.find(7) # Lucy
root.find(4) # John
print("---------------------")

# REMOVES A NODE

'''Note that removing a node is a chain.
Cut off one branch, the other branches collapse
This can be fixed by rebalancing the tree, but we won't
dive that deep in this lesson.
'''
print("REMOVING USERS. . .")
root.remove(3) # 1, 2 and 3 are dropped
root.remove(5) # 5 dropped
root.remove(2) # NODE DOESN'T EXIST
print("---------------------")
# FINDING THE PEOPLE ON THE NEW TREE
# current tree = [4, 6, 7]
print("FINDING USERS. . .")
root.find(4) # John
root.find(6) # Peter
root.find(2) # DOESNT EXIST
print("---------------------")
# ITERATES THROUGH ALL THE USERS IN THE TREE
print("ALL USERS. . .")
root.find_all()
print("---------------------")
