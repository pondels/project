import random

class UniqueNum:

    def __init__(self, example_set):
        self.set = example_set

    def show_set(self):
        '''
            Will show all unique items in the set
        '''
        for number in self.set:
            print(number, end=' ')
        print('\n')

    def add_range(self, start, end):
        '''
            Adds a number to the set.

            Will not add duplicate numbers due
            to the nature of a set.
        '''
        for num in range(start, end + 1):
            self.set.add(num)

    def add_num(self, num):
        '''
            Adds a number to the set

            Will not add if the number already exists within the set
        '''
        self.set.add(num)

    def find(self, number):
        '''
            Looks for a given number in the set
        '''
        for num in list(self.set):
            if num == number:
                print(f"{number} found in the set!")
                return

        print(f"{number} was not found in the set!")

    def find_index(self, index):
        '''
            Returns the value of the given index of the set
        '''
        if index <= len(list(self.set)): # Index value is within bounds of the set
            print(list(self.set)[index])
        else:
            print("INDEX OUT OF RANGE")

    def remove_num(self, amount):
        '''
            removes a random amount of numbers from the set
        '''

        if amount < len(list(self.set)):
            
            sorted_array = [] # Used for formatting a sorted list of removed numbers
            print("NUMBERS TO REMOVE: ", end='')

            for _ in range(amount):
                remove_num = random.choice(list(self.set)) # Generates a random number from the set
                sorted_array.append(remove_num)
                self.set.remove(remove_num) # Removes the number from the set
            
            sorted_array.sort() # Sorts the array to format to the user
            for number in sorted_array:
                print(number, end=' ')
                
            print('\n')

        else: # They are trying to remove more than there is in the set
            print("TOO MANY NUMBERS BEING REMOVED")


# Defining the set
example_set = set()
for num in range(101):
    example_set.add(num) # Funnelling in 101 numbers into the set

# Defining the class
uniquenum = UniqueNum(example_set)
print("STARTING SET")
uniquenum.show_set()
print("--------------------------------\n")

# Adds numbers from 50 - 150
print("PROBLEM SET NUMBER 1")
uniquenum.add_range(50, 150) # new numbers 101 - 150
uniquenum.show_set()
print("--------------------------------\n")

# Adds specific numbers

# Notice how adding any number will automatically be sorted into the set
print("PROBLEM SET NUMBER 2")
uniquenum.add_num(-1) # -1 Added
uniquenum.add_num(-15) # -15 Added
uniquenum.add_num(58) # Nothing should happen
uniquenum.add_num(278) # 278 Added
uniquenum.add_num(162) # 162 Added
uniquenum.show_set()
print("--------------------------------\n")

# Checks if a value exists within the set | O(n)
print("PROBLEM SET NUMBER 3")
uniquenum.find(27) # True
uniquenum.find(151) # False
uniquenum.find(17) # True
uniquenum.find(150) # True
uniquenum.find(-16) # False
print("--------------------------------\n")

# Prints what is in a certain index within the set 
# Due to the nature of this set, the index should return the same number as the index
print("PROBLEM SET NUMBER 4")
uniquenum.find_index(15) # 15
uniquenum.find_index(160) # INDEX OUT OF RANGE
uniquenum.find_index(58) # 58
print("--------------------------------")

# Removes a given amount of random numbers from the set
print("PROBLEM SET NUMBER 5")
uniquenum.remove_num(10) # Removes 10 randomly selected numbers from the set
uniquenum.show_set()
uniquenum.remove_num(150) # TOO MANY NUMBERS BEING REMOVED | No need to print the same set
print("--------------------------------\n")