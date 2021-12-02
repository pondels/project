

class UniqueNames:

    def __init__(self):
        self.names = set()

    def create_set(self, list_of_names):
        '''
            Adds each unique name to the set
        '''
        # Your Code Goes shere
        pass

    def show_set(self):
        '''
            Shows all values in the set
        '''
        print(self.names)

    def count_unique(self):
        '''
            Prints the amount of unique names in the set
        '''
        # Your Code Goes Here
        pass

    def remove_name(self, name):
        '''
            Removes a given name from the set
        '''
        # Your Code Goes Here
        pass

    def find_index(self, index):
        '''
            finds the index of a user
        '''
        if index > len(list(self.names)):
            print("INDEX OUT OF RANGE")
        else:
            # Your Code Goes Here
            pass


# Initializing the class
uniquenames = UniqueNames()

# PROBLEM NUMBER 1
# Creating the set of 50 unique names
print("PROBLEM SET NUMBER 1")
print()
list_of_names = ["Jessie", "Walker", "Liberty", "Selena", "Hailey", "Braden", "Camila", "Camila", "Jarrett", "Damion", "Rayna", "Messiah", "Lillian", "Garrett", "Yoselin", "Wilson", "Zane", "Elyse", "Ayana", "Paola", "Simeon", "Ximena", "Layla", "Lillian", "Marlene", "Hazel", "Azul", "Micaela", "Liam", "Braylen", "Jordon", "Jared", "Jaquan", "Cason", "Alia", "Annabelle", "Victoria", "Kasey", "Tanner", "Jaylen", "Lizeth", "Nathalia", "Addyson", "Celia", "Naomi", "Jimena", "Drake", "Cole", "Yoselin", "Bryanna", "Pablo", "Jazlyn", "Odin", "Urijah", "Haylee", "Katie", "Makaila", "Danika", "Paris", "Abbigail", "Deangelo", "Thalia", "Frances", "Amir", "Albert", "Maximilian", "Tristen", "Kendal", "Sonia", "Morgan", "Jaidyn", "Slade", "Shaun", "Cooper", "Damion", "Ariella", "Sydnee", "Greyson", "George", "Levi", "Yadiel", "Jadyn", "Eliana", "Isaias", "Emanuel", "Tristen", "Sincere", "Hailee", "Geovanni", "Joslyn", "Rohan", "Aidan", "Joey", "Julia", "Alexandria", "Damari", "Isabella", "Augustus", "Jaylin", "Bella"]

uniquenames.create_set(list_of_names) # There should be 5 duplicates
uniquenames.show_set() # Set should be populated
print("----------------------------------")
print()

# PROBLEM NUMBER 2
# Prints the amount of unique names in the array
print("PROBLEM SET NUMBER 2")
print()
uniquenames.count_unique() # 95 unique names
print("----------------------------------")
print()

# PROBLEM NUMBER 3
# Removes Names from the list
print("PROBLEM SET NUMBER 3")
uniquenames.remove_name("Lillian")
uniquenames.remove_name("Cason")
uniquenames.remove_name("Brent") # Throw Error | Name Not In Set
uniquenames.remove_name("Lizeth")
uniquenames.count_unique() # 92 unique names
print("----------------------------------")
print()

# PROBLEM NUMBER 4
# 
print("PROBLEM SET NUMBER 4")
uniquenames.find_index(15)
uniquenames.find_index(0)
uniquenames.find_index(71)
uniquenames.find_index(98) # Index Out Of Range
uniquenames.find_index(44)
print("----------------------------------")
print()