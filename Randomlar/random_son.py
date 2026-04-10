import random

def son_ol(matn = "Son kiriting: "):
    son = input(matn)

    while not son.isdigit():
        son = input("Faqat son kiriting!: ")

    return int(son)

def main():
    print("="*30)
    print("O'ylagan sonimni top!")
    print("="*30)

    ss = random.randint(1, 10)
    limit = 3

    while True:
        print("Sizda", limit, "ta urunish bor.")
        son = son_ol()
        while son > 10:
            son = son_ol("Faqat 1 va 10 lar va ular oralig'ida son kiriting!")
        if son > ss:
            print("Men o'ylagan son kichikroq.")
        elif son < ss:
            print("Men o'ylagan son kattaroq.")
        else:
            print("Tanlovingiz shartlarga mos kelsin!")

        limit -= 1
        if limit == 0:
            print("Urunishlar tugadi. Siz yutqazdingiz!")
            print("Men", ss, "sonin o'ylagan edim.")
            break


main