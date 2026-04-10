a = int(input("Sonni kiriting: "))

def tekshir(son):
    if 0>a:
        return "Son manfiy"
    else:
        return "Son musbat"
print(tekshir(a))



#Parametr bilan ishlash:



def tekshir(son):
    if son > 0:
        return "musbat"
    else:
        return "manfiy yoki 0"
print(tekshir(-7))
