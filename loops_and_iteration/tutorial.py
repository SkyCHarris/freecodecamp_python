# While Loop

n = 5
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

# Loops have 'iteration variables' that change each time through a loop. Often these iteration variables go through a sequence of numbers

# Infinite Loop (bad, runs infinitely)

n = 5
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

# Another Loop (zero-trip)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

# Breaking Out of a Loop

# The break statement ends the current loop and jumps to the statement immediately following the loop
# It is like a loop test that can happen anywhere in the body of the loop

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

# Finishing an Iteration with Continue

# The continue statement ends the current iteration and jumps to the top of the loop to start the next iteration

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')