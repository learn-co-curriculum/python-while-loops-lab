
# While Loops Lab

## Introduction
In this lab, we will be practicing while loops. We will use them to perform a few different actions until the condition we set becomes false. 

## Objectives
* Understand how wile loops work
* See how while loops can replace simple for loops with conditional statements

## Instructions
Use while loops to perform the below operations and get the expected return values


```python
slices_of_pie = 6
slices_eaten = 0
# use a while loop to eat each slice of pie
# add eaxh slice to the slices_eaten variable
while slices_of_pie > 0:
    slices_of_pie -= 1
    slices_eaten += 1
```


```python
time_for_breakfast = 1468 # in seconds
number_of_cooked_pancakes = 0
# use a while loop to make yourself 5 pancakes for breakfast
# each pancake takes 27 seconds to cook on each side
# you must decrease the time_for_breakfast each time you 
# add a pancake to the skilled or flip a pancake (i.e. 2 times per pancake)
# there is only room for one pancake at a time
while number_of_cooked_pancakes < 5:
    if time_for_breakfast > 54:
        print("pour flapjack")
        time_for_breakfast -= 27
        print("flip flapjack")
        time_for_breakfast -= 27
        print("that's a fine pancake")
        number_of_cooked_pancakes += 1
    else:
        print("No time for more pancakes!! >:(")
```

> **Hint:** You may find the [remove method](https://www.programiz.com/python-programming/methods/list/remove) to be useful for the next problem


```python
line_of_hungry_patrons = list(range(0,30))
fed_patrons = []
# use a while loop to to feed the hungry patrons with an even number
# add the patrons with an even ticket number to the fed_patrons list
# and remove the patrons from the line_of_hungry_patrons

index = 0
while len(fed_patrons) < len(line_of_hungry_patrons):
    patron = line_of_hungry_patrons[index]
    if patron % 2 == 0:
        index += 1
        fed_patrons.append(patron)
        line_of_hungry_patrons.remove(patron)

print(fed_patrons, line_of_hungry_patrons, len(fed_patrons))
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28] [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29] 15


## Summary

In this lab, we practiced using while loops to perform different operations. While loops continue executing their block of code until the condition given is false. This is useful for instances where we do not have a collection or need a collection to solve our problem, especially when we would only like to stop the process after we have met a certain condition.
