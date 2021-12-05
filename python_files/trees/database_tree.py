class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        
        if data == node.data:
            return
        elif data['id'] < node.data['id']:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)

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
