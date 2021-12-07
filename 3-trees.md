# `Welcome to Binary Trees!`
Binary trees are cool, as they are just like branches to a tree, and are very useful for data.
But what is a binary tree, and how are they used in the real world?

Before we look into what a binary tree is, we need to understand one fundamental concept in programming.

## `Recursion`
#
Recursion is a difficult concept to master, but let's look at a line of code to understand what it is, and how it works.

```python
    def recursive_function(count):
        if count > 0:
            recursive_function(count - 1)
            print("Recursion Happened!")

    recursive_function(5)
```
Recursion is the concept that you have what's called a "base case" or an event to return when calling a function. When you use recursion, you are calling and recalling a function until the base case has been reached.

In this example, the number 5 is being fed into the function. The base case in this example is count being less than or equal to zero. 5 is greater than zero, so it plugs 5 - 1 into the function again. This happens recursively until you get recursive_function(0). 

Since 0 is less than or equal to zero, it finishes the line of code and prints "Recursion Happened!" Then it has a chain event of the lines finishing, since the last event just finished. It will then continue the chain of print statements. This results in the function running 5 times, leading to 5 print statements.

## `Binary Tree Example`
#

Let's look at an example of some code and an image of a binary tree.

The [following code](python_files/trees/binary_tree.py) creates this binary tree.
<br>
<img src="picture_files/binary_tree.png" width = 250px></img>

While looking at the code, let's dissect it line for line to see how this code is creating the binary tree.

There is a class called BST (binary search tree) and an imbedded class called Node. The node class defines a single point in the tree, having a data point, and the numbers to its right and left. The numbers to its left will always be less than it. Vice versa for the right. The root is always one number, the starting point. In this case, the root is 8.

Let's look at the insert function.

The insert function is very complex function, but let's look at it very carefully.

First the insert function is called and checks if the root has been defined, if so, it will called the _insert function, placing in the number desired to input, and the root.

The _insert function checks if the data is equal to the node's data, if so, nothing is added in, since the data already exists.

If the data is less than the node's data it will check if the left data exists already, if not, it sets the left data point to the data desired. If data already exists there, it has to compare to the following data point, therefore recursion happens. It will throw in the data and the left node. From there this will repeat until the left is empty.

This is the same for the right node, if the data is greater than the data of the node, it should be the node's right data point and is therefore set so. If data already exists there, the same recursion happens, but this time checking the right node.

This leads to the image you see above. Feel free to study to program more as necessary to get a feel for more depth on what exactly is happening.

## `Performance`
#
With all of that being said, what the heck is the performance of a binary search tree?

Binary search tree's have one efficiency throughout itself, and it's $O(log(n))$ But why is it this effiency?

If you remember from earlier, $O(log(n))$ is usually when you cut down your searching in half through every iteration, making something more and more efficient as you look for data, insert, or delete data. 

A binary search tree does this by checking for a boolean variable. Let's assume using the same picture again, we're looking for the number 6. Take this dynamic array as an example for the binary tree

```python
    binary_tree = [1, 3, 4, 6, 7, 8, 10, 13, 14]
```

Since 6 is less than 8 (the root), it will check anything less than 8.

```python
    binary_tree = [1, 3, 4, 6, 7]
```

Since it's cut in half, we already have $O(log(n))$. This continues 

This continues down the tree.

```python
    binary_tree = [1, 3, 4, 6, 7] # Node Here is 3
    >> [4, 6, 7] # 6 Is hreater than 3, so we have this list
    binary_tree = [4, 6, 7] # Node here is 6
    >> '6 Found in 3 Iterations'
```

## `Problems`
#
As you can see, binary search trees are very useful, as they are super efficient, and they seem to have no problems, however all things have their problems, and that leaves no exception to binary search trees.

Here are a couple examples.

As you may know, binary search trees use recursion and not other forms of loops. One thing I didn't mention, was recursion takes up memory, and a system will only allow so much recursion depth, before reaching it maximum limit for memory reached.

This usually happens when you have an unbalanced tree.

Take this for example. You start with 1 as your root and keep adding numbers higher in progression to the root. Well you don't have a tree, you just have more of a linked list, or an array of sorts. This leads to $0(n)$ in efficiency and can lead to maximum recursion depth, losing memory in the process.

While there are ways of balancing a tree to fix it for better balancing, without the balancing algorithm, you have massive problems with the tree.

## `Usefulness`
#
Now how are binary trees useful? As you saw with the number example, you can sort numbers in order, having a tree sorted by numbers. Another way of using binary trees in the real world could be for database management.

Let's assume you are wanting to search for someone in a database with the ID 15 and you have 63 people in your database with their own unique ID. You can sort the ID's using a binary search tree and then find the user you're looking for a lot quicker.

## `Example Problem`
#
Speaking on a database, let's look at this example problem with how to sort people in a database via ID. 
Click [here](python_files/trees/database_tree.py) to see the example problem with the binary tree.

## `Solve Your Own Problem`
#
Example Situation: You are at your new internship job when your boss gives you your first task. You are to take the given binary tree information and solve the 5 problems that are listed in the program. The tree consists of a heirarchy of milk prices, and you are to find the given information about the milk. Click [here](python_files/trees/milk.py) to start your problem set. When you are finished, click [here](python_files/trees/milk_solution.py) to view the solution.