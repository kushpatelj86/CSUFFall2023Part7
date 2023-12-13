class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age




list = [1,3,5,6]
def modify(item):
    modi = [] + item
    return modi



class FoodMyClass:
    name = "Chicke"
    calories = 543
    
    def __init__(self, stringfds):
        self.stringfds = stringfds
        self.stringfds += "Initialized"


    def double_i(self):
         dub = self.calories * 2
         return dub


food = FoodMyClass("Chicken",12)
food.double_i()