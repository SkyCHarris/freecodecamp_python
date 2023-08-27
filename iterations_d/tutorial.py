# Counting in a Loop

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork +1
    print(zork, thing)
print('After', zork)

# -To count how many times we execute a loop, we introduce a 'counter variable' that starts at 0 and we add one to it each time through the loop

# Summing in a Loop

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# -To add up a value we encounter in a loop, we introduce a 'sum variable' that starts at 0 and we add the value to the sum each time through the loop

# Finding the Average in a Loop

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# -An average just combines the counting and sum patterns and divides when the loop is done

# Filtering in a Loop

print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large number',value)
print('After')

# -We use an if statement in the loop to catch / filter the values we are looking for

# Search Using a Boolean Variable

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)

# -If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for

# How to Find the Largest Value

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# How to Find the Smallest Value

smallest_so_far = 100
print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print('After', smallest_so_far)

# -This is an inferior way of looking at the problem, trying to use an arbitrarily small or large number. What we need to do is capture the first number in the array, since it's both the smallest and largest number
# -We use the 'None' type.
# -Integer, floating point, string, boolean, none.
# -None type is a special marker in that it only has one value. None. None is a constant.
# -None is often used to indicate emptiness, NOT non-existence.

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# The 'is' and 'is not' Operators

smallest = None
print('Before')
for value in [3, 41, 12, 9, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)

print('After', smallest)

# -Python has an 'is' operator that can be used in logical expressions
# -Implies "is the same as"
# -Similar to, but stronger than ==
# -'is not' also is a logical operator
# -Demands equality in 'type' and 'value' of the variable
# -Generally use on boolean and None types