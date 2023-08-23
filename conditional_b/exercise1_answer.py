hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
reg_pay = hours * rate
""" print(hours, rate)
pay = hours * rate
print("Pay:", pay) """

if hours > 40 :
    print("Overtime")
    over_pay = (hours - 40.0) * (rate * 0.5)
    print(reg_pay + over_pay)
else :
    print("Regular")
    print(reg_pay)
    