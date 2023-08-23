hours = float(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
extra_hours = hours - 40
extra_rate = rate / 2
pay = hours * rate
extra_hours_pay = extra_hours * extra_rate



if hours > 40 :
   print("Pay:", pay + extra_hours_pay)
else: 
    print("Pay:", pay)

# Why tf does this work
# Extra rate should be rate * 1.5 for overtime, shouldn't it? Not / 2

# It's because you're only getting an extra .5 for each overtime hour worked, NOT an extra 1.5!
