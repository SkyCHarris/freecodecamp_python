
hours = (input('Enter Hours:'))
rate = (input('Enter Rate:'))

try:
    float_hours = float(hours)
    float_rate = float(rate)
except:
    print("Error. Please enter a numeric value")
    quit()
# Need the quit() to escape and not run the rest of the code below BECAUSE we don't have a way to deal with a string input like 'ten'

reg_pay = float_hours * float_rate

if float_hours > 40 :
    over_pay = (float_hours - 40.0) * (float_rate * 0.5)
    print(reg_pay + over_pay)
else :
    print("Regular")
    print(reg_pay)
    