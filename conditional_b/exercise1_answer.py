hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
reg_pay = hours * rate

if hours > 40 :
    over_pay = (hours - 40.0) * (rate * 0.5)
    print(reg_pay + over_pay)
else :
    print("Regular")
    print(reg_pay)
    