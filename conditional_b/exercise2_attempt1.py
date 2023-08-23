
hours = (input('Enter Hours:'))
rate = (input('Enter Rate:'))

try:
    float_hours = float(hours)
    float_rate = float(rate)
except:
    print("Error. Please enter a numeric value")
    quit()

reg_pay = float_hours * float_rate

if float_hours > 40 :
    over_pay = (float_hours - 40.0) * (float_rate * 0.5)
    print(reg_pay + over_pay)
else :
    print("Regular")
    print(reg_pay)
    