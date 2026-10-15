# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

notfish2 = []
for item in animals:
    if item != "goldfish":
        notfish2.append(item)

print(not_fish)
print(notfish2)



# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same