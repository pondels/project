
class Queue:

    def __init__(self):
        self.caller_list = []

    def add_caller(self, caller):
        '''
            Adds a caller to the caller list
        '''
        self.caller_list.append(caller)

    def next_caller(self):
        '''
            Removes the next caller in line from the caller list
        '''
        if len(self.caller_list) != 0:
            self.caller_list.pop(0)
        else:
            print("No caller on the line!")

    def view_callers(self):
        '''
            Views the callers in the caller list
        '''
        print(self.caller_list)

# Initialize the queue
queue = Queue()

# PROBLEM NUMBER 1
# Adds a caller to a waitlist
queue.add_caller("Sally Jones")
queue.view_callers() # ["Sally Jones"]

queue.add_caller("Benjamin Allanson")
queue.view_callers() # ["Sally Jones", "Benjamin Allanson"]

queue.add_caller("Joseph Feran")
queue.view_callers() # ["Sally Jones", "Benjamin Allanson", "Joseph Feran"]

# PROBLEM NUMBER 2
# Takes in the next caller
queue.next_caller()
queue.view_callers() # ["Benjamin Allanson", "Joseph Feran"]

queue.next_caller()
queue.view_callers() # ["Joseph Feran"]

queue.next_caller()
queue.next_caller() # No caller on the line!

queue.view_callers() # []