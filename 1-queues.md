# Welcome to Queues!
Queues are very cool, but what exactly does a queue look like in code form?

Take this code for example
```python
    queue = [1, 2, 3, 4, 5, 6]
```
A queue is simply a dynamic array, as it automatically adjusts itself based on the amount of datapoints within the list object.

Assuming you want to add to the queue, you will obviously place the data in the back of the list, just like a queue. If you want the next item in the array to be removed, you will simply remove this from the from of the array.
```python
    queue = [1, 2, 3, 4, 5, 6]
    queue.append(7)
    >> [1, 2, 3, 4, 5, 6, 7]
    queue.pop(0)
    >> [2, 3, 4, 5, 6, 7]
```
## Usefulness
#
Queues are very useful in programming, as it treats certain blocks as `priority`. Think of it like a line at a grocery store. `You start in the back and make your way forward` until it's your time to check out your groceries. This is the same for queues.

When you want to create a queue, let's say a user for a game, you want to make sure they don't get randomly chosen, but treat it like a priority line, and that they must wait their turn.

## Efficiency
#
A queue is very efficient, as you always know where your data is being fetched from. The front, or the back. Thas makes this algorithm O(1) efficiency, which makes this type of algorithm very efficient.

HOWEVER, while you may know where your information is, it is always dependant on where your information is being pulled. Take this for example.
```python
    example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    example_list.append(10)
    >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    example_list.pop(0)
    >> [_, 2, 3, 4, 5, 6, 7, 8, 9, 10] # The list will never look like this, this is just an example of the item being removed.
    
    >> [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # You can see that removing the first item left a gap. This means that all the information has to shift left 1, making removing from the front, O(n), whereas taking or adding to the back doesn't effect any other data, making it O(1).
```

## Problems to Solve
#
Some may ask what the purpose of queues may be, and how they serve in the real world? There are many purposes for queues, but the most relevant purpose in my personal experience is priority for users.

This takes me to our first example problem.

## `Example Problem`
#
Click [here](python_files/queues/server-example.py) to view a sample solution to visualize someone being queued for a match on a video game.

## `Solve Your Own Problem`
#
Now that you understand how queues work, now is the time to solve your own problem. There will be a class created with some code that will break, and your job is to solve the problem by completing the program. Click [here](python_files/queues/callers.py) to get started. When you're done, you can view the solution [here](python_files/queues/callers-solution.py)