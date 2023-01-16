
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
    
    
def myfunction_subtract(x,y):
    subt = x-y
    return subt

def myfunction_Division(x,y):
    divi = x/y
    return divi


add = myfunction_sum(10,20)
print("Sum =",add)

multipli = myfunction_multiply(10,20)
print("Multiply =",multipli)

subtract = myfunction_subtract(10,20)
print("Difference =",subtract)

divide = myfunction_Division(10,20)
print("Divide =",divide)
