# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers.
# If the users enters anything other than a number, detect their mistake using 'try' and 'except' and print an error message and skip to the next number

number = 0
total = 0.0

while True :
    sval = input('Enter a number:')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
    # print(fval)
    number = number +1
    total = total + fval

# print('All Done!')
print(total, number, total/number  )




