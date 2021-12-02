# `Welcome to Sets!`
Sets are usually defined as they are named. It is a set of values that are all unique. Now how does that look in coding terms? Well let's look at this for example.
```python
    set = {"John", "Sally", "Bob", "Joe"}
```
Notice how this set does not have duplicate values. That's because a set, like a dictionary cannot have duplicate values.

Let's look at the following code to see how sets function

```python
    my_set = set()
    my_set.add(1)
    >> {1}
    my_set.add(4)
    >> {1, 4}
    my_set.add(1)
    >> {1, 4}
```
Notice how no duplicates are added, this is because sets are like dictionaries and will only store information if it does not already coexist within the set.

## `Performance`
#
The performance of a set can always be different, but for the most part, you are dealing with $O(n)$ because you iterate through the values unless you know that a value exists in the set. In this case it would be $O(1)$.

## `Problems`
#
There's at lease one problem with sets, and it's the fact that it's a set. You are unable to have duplicate values. Take this for example. Let's assume you are wanting to find all possible users in a database. A set probably wouldn't be the best option if you are querying the users by first name, since it is possible to have multiple people with the same first name.

You have to get creative with sets. In a case like this, you will want to grab an ID of a user, since ID's are unique to each person.

## `Usefulness`
#
A set is useful in many ways. Maybe you have data that is unique to itself and you want to keep it organized. Maybe you have a set of pokemon cards that you want to store in a database and want to make sure you don't count duplicate cards. Whatever the reason is, sets can be used for many reasons.

Let's look at a problem with sets
## `Example Problem`
#
Click [here](python_files/sets/unique-num-example.py) to see an example problem with sets.

## `Solve Your Own Problem`
#
Now that you understand what a set is and what they are used for, let's start a problem for you to solve! In this code you will be going through each problem in order. Each problem should either be its own or should solve future cases. Click [here]() to start your lesson. Go ahead and check how you did compared to the solution [here]().
