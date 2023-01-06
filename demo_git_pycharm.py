
from datetime import date

print ("Hello")

today = date.today()
print("Today's date:", today)

def myfunction(x,y):
    sum = x+y
    return sum

add = myfunction(10,20)
print("Sum =",add)