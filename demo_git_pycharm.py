
from datetime import date

print ("Hello")

today = date.today()
print("Today's date:", today)

def myfunction_sum(x,y):
    sum = x+y
    return sum

def myfunction_multiply(x,y):
    multipli = x*y
    return multipli

add = myfunction_sum(10,20)
multipli = myfunction_multipli(10,20)
print("Sum =",add)
print("Multiply =",multipli)
