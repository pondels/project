
class Queue:

    def __init__(self):
        '''
            DEFINING THE QUEUE
        '''
        self.queue = []

    def queue_join(self, player):
        '''
            ADDS THE PLAYER TO THE QUEUE
        '''
        self.queue.append(player)

    def queue_leave(self, player):
        '''
            REMOVES A PLAYER FROM THE QUEUE

            ONLY IF THE PLAYER IS IN THE QUEUE
        '''
        if player in self.queue:
            self.queue.remove(player)
        else:
            print("PLAYER NOT FOUND")

    def view_queue(self):
        '''
            PRINTS OFF THE QUEUE
        '''
        print(self.queue)

    def add_queue(self, queue):
        '''
            ADDS ANOTHER PRE-EXISTING QUEUE TO THE CURRENT QUEUE
        '''
        self.queue += queue

    def add_to_game(self):
        '''
            TAKES A PLAYER FROM THE QUEUE AND "ADDS" THEM TO THE GAME

            ONLY REMOVES IF PLAYERS ARE IN THE QUEUE
        '''
        if len(self.queue) != 0:
            self.queue.pop(0)
        else:
            print("QUEUE EMPTY")

# Initializes a queue
queryOperator = Queue()

### Problem Set 1
# People joining the game

# John and sally want to join the game
queryOperator.queue_join('John')
queryOperator.queue_join('Sally')
queryOperator.view_queue()

# Peter joins after Sally
queryOperator.queue_join('Peter')
queryOperator.view_queue()

## Problem Set 2
# People leaving the queue

# Sally leaves the queue
queryOperator.queue_leave('Sally')
queryOperator.view_queue()

## Problem Set 3
# Another queue small enough merges to the currect queue

# Craig Bob and Jeffery were in a smaller queue from a game
# that got abandoned and are being added to the new queue
queryOperator.add_queue(['Craig', 'Bob', 'Jeffery'])
queryOperator.view_queue()

## Problem Set 4
# The system takes players in the game

# John Peter and Craig are taken into the game
queryOperator.add_to_game()
queryOperator.add_to_game()
queryOperator.add_to_game()
queryOperator.view_queue()