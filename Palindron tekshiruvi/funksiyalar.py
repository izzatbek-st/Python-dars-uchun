def get_text():
    a = input("So'zni kiriting: ")
    while not a.isalpha() or len(a.split()) != 1 >= 2:
        a = input("Faqat 1 ta so'z kiriting kiriting: ")
    return str(a)

def teskari_soz(matn):
    return matn[::-1]

def tekshir():
    soz = get_text()
    teskari = teskari_soz(soz)
    
    if soz == teskari:
        print("So'z polindrom.")
    else:
        print("So'z polindrom emas.")

def main():
    tekshir()