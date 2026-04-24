class Oquvchi:
    def __init__(self, ism):
        self.ism = ism

while True:
    kiritilgan_ism = input("Ism: ")
    yangi_oquvchi = Oquvchi(kiritilgan_ism)
    
    with open("Ro'yxat", "a") as fayl:
        fayl.write(yangi_oquvchi.ism + "\n")
        
    print(yangi_oquvchi.ism, "faylga saqlandi")