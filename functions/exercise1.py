# Rewrite pay computation time-and-a-half for overtime, create function called computepay which takes two parameters (hours and rate)

def computepay(hours, rate) :
    if hours > 40 :
        reg_pay = hours * rate
        over_pay = (hours - 40.0) * (rate * 0.5)
        total_pay = reg_pay + over_pay
    else :
        total_pay = hours * rate
    print("Pay:", total_pay)
    return total_pay

your_hours = (input('Enter Hours:'))
your_rate = (input('Enter Rate:'))
float_hours = float(your_hours)
float_rate = float(your_rate)

total_pay = computepay(float_hours, float_rate)

print(total_pay)



    



