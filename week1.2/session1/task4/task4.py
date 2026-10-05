# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#items present in both dictionaries
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#it joins both lists without adding duplicates
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("an item")
print(fruit)

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
thing = fruit.symmetric_difference(vegetables)
print(thing)
