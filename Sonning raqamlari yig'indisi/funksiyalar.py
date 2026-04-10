def son_ol():
    a = input("3 xonali son kiriting: ")
    return int(a)

def hisobla():
    son = son_ol()
    yuzlar = son // 100
    onlar = (son-yuzlar*100) // 10
    birlar = son % 10
    yigindi = yuzlar + onlar + birlar
    print(f"Sonning raqamlar yig'indisi {yigindi}ga teng.")

def main():
    hisobla()