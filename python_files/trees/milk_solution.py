
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
        elif data['price'] < node.data['price']: # Price is less than the data
            if node.left is None: # No data found, insert it in the left
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None: # Number is greater than the data
                node.right = BST.Node(data) # No data found, insert in right
            else:
                self._insert(data, node.right)

    def find(self, price):
        if price == self.root.data['price']: # Price is the root
            print(self.root.data['brand'])
        else:
            self._find(price, self.root)
    
    def _find(self, price, node):
        if node == None:
            print("BRAND NOT FOUND")
        elif node.data == None or node.data == None:
            print("BRAND NOT FOUND")
        else:
            if price == node.data['price']: # Price Matched
                print(node.data['brand'])
            elif price > node.data['price']: # Price greater than node's price, check right
                self._find(price, node.right)
            else: # Price less than node's price, check left
                self._find(price, node.left)

    def find_all(self):
        if self.root.left == None and self.root.right == None:
            print(self.root.data['brand'])
        else:
            self._find_all(self.root)

    def _find_all(self, node):
        if node.data == None:
            return
        if node.left != None:
            if node.left.data != None:
                self._find_all(node.left)
        if node.right != None:
            if node.right.data != None:
                self._find_all(node.right)
        print(node.data['brand'])
        return

    def remove(self, price):
        if price == self.root.data['price']:
            self.root = None
        else:
            self._remove(price, self.root)

    def _remove(self, price, node):
        if node.data == None:
            print("BRAND NOT FOUND")
            return
        if node.data['price'] == price: # Brand Found
            print(f"REMOVING {node.data['brand']}")
            node.data = None
            node.right = None
            node.left = None
        elif price > node.data['price']: # Price Greater than node, check right
            self._remove(price, node.right)
        else: # Price Less than node, check left
            self._remove(price, node.left)

    def find_cheapest(self):
        if self.root.left.data == None: # Next node doesn't exist
            if self.root != None:
                print(self.root.data['brand'])
        else:
            self._find_cheapest(self.root) # Recursion starts
    
    def _find_cheapest(self, node):
        if node.left == None:
            print(node.data['brand'])
        else:
            self._find_cheapest(node.left) # Not the cheapest, keep going

    def find_expensive(self):
        if self.root.right == None: # Next node doesn't exist
            if self.root != None:
                print(self.root.data['brand'])
        else:
            self._find_expensive(self.root) # Recursion starts
    
    def _find_expensive(self, node):
        if node.right == None:
            print(node.data['brand'])
        else: # Not the most expensive, keep going
            self._find_expensive(node.right)

root = BST()

database = [
    {'price': 3.19, 'brand': 'Silk'},
    {'price': 2.99, 'brand': 'Great Value'},
    {'price': 3.59, 'brand': 'Meadow Gold'},
    {'price': 3.09, 'brand': 'Food Club'},
    {'price': 2.79, 'brand': 'True Moo'},
    {'price': 3.39, 'brand': 'Kroger'},
    {'price': 4.99, 'brand': 'Fairlife'}
    
]

# INSERTING EACH PERSON INTO THE TREE
for milk in database:
    root.insert(milk)

'''CURRENT TREE (by price)
                    Silk
              /             \\
    Great Value             Meadow Gold
    /          \\           /          \\
True Moo     Food Club  Kroger        FairLife

'''

# FINDING A PERSON IN THE TREE
print("FINDING BRAND. . .")
root.find(2.79) # True Moo
root.find(3.59) # Meadow Gold
root.find(6.49) # Nothing Found!
root.find(4.99) # FairLife
print("---------------------")

# FINDING THE CHEAPEST MILK
print("CHEAPEST MILK: ", end='')
root.find_cheapest() # TrueMoo
print("---------------------")

# FINDING THE MOST EXPENSIVE MILK
print("MOST EXPENSIVE MILK: ", end='')
root.find_expensive() # FairLife
print("---------------------")

# REMOVING A MILK BY PRICE
print("REMOVING BRANDS BY PRICE. . .")
root.remove(2.99) # Removes Great Value, True Moo and Food Club
root.remove(4.99) # Removes Fairlife
root.remove(2.79) # TrueMoo Shouldn't Exist
print("---------------------")

# FINDING THE MILK ON THE NEW TREE
print("FINDING BRANDS. . .")
root.find(2.79) # Verify That TrueMoo Doesn't Exist
root.find(3.19) # Silk Exists
root.find(3.39) # Kroger Exists
print("---------------------")

# ITERATES THROUGH ALL THE BRANDS IN THE TREE
print("ALL BRANDS. . .")
root.find_all() # Kroger, Meadow Gold, and Silk
print("---------------------")
