class Car:

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        
    def honk(self):
        print("Beep beep")

    def mode_l(self):
        print(self.model)
    
cobalt = Car("cobalt", "black", "2015")

cobalt.mode_l()