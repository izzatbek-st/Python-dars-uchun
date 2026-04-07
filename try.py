def son_ol():
    return float(input("Son kiriting: "))

def salom_ber():
    d = input("Nimadir yoz:")
    if d.lower() == "hi":
        print("Salom, Izzatbek!")
    else:
        print("Hi di")


def kalkulyator():
    while True:
        amal = input("Amal tanla (+, -, * yoki exit): ")

        if amal.lower() == "exit":
            break

        a = float(input("Birinchi son: "))
        b = float(input("Ikkinchi son: "))

        if amal == "+":
            print("Natija:", a + b)
        elif amal == "-":
            print("Natija:", a - b)
        elif amal == "*":
            print("Natija:", a * b)
        else:
            print("Noto‘g‘ri amal!")


def new_func():
    print("Noto‘g‘ri tanlov!")

while True:
    tanlov = input("1 - Salom ber | 2 - Kalkulyator | exit >>> ")

    if tanlov == "1":
        salom_ber()
    elif tanlov == "2":
        kalkulyator()
    elif tanlov.lower() == "exit" or "stop":
        break
    else:
        new_func() 