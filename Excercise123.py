class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age




list = [1,3,5,6]
def modify(item):
    modi = [] + item
    return modi



class FoodMyClass:
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories
    
    
    def double_i(self):
         dub = self.calories * 2
         return dub


food = FoodMyClass("Chicken",12)