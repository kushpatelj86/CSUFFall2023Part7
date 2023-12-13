import Excercise123
import Excerise4



print(Excercise123.modify([1,3]))
print(Excerise4.modify([2]))


class Car:
    def __init__(self,name,year):
        self.name = name
        self.year = year

car1 = Car("Toyota Camry",2001)
del car1.year


var1 = 3
def num1():
    var2 = 4 + var1
    def num2():
        var3 = 5 + var2
    global var4
    var4=10 
print(var1)



def num1():
    var2 = 4 + var1
    def num2():
        var3 = 5 + var2
    num2()
    print("num1", var2)


