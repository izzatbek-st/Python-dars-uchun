class Human:
    def __init__(self, name: str, bornyear: int):
        self.name = name
        self.bornyear = bornyear
    
    def breathe(self):
        print("Nafas olyapti")
    def canwalk(self):
        print("Yura oladi")


class Dasturchi(Human):
    def coding(self):
        print("Kod yoza oladi")

class Builder(Human):
    def building(self):
        print("Qura oladi")


bobur = Dasturchi("Bobur", 2006)
ali = Builder("Ali", 2004)

print(ali.bornyear)