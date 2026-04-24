class Dog:
    
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def woof(self):
        print("Woof Woof")
    
hotdog = Dog("It", "Black", "3")

hotdog.woof()