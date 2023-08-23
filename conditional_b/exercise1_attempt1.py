hours = input('Enter hours:')
rate = input('Enter rate:')

extra_hours = int(hours) - 40

if int(hours) > 40 :
    print((int(rate) * extra_hours + int(rate) * int(hours)))
elif int(hours) < 40 :
    print(int(hours))
else :
    print('Error')
    
#Returning 500
