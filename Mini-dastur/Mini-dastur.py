while True:

    tekshiruv = input("\nHisobingiz mavjud bo'lsa 1, agar mavjud bo'lmasa 2 ni kiriting, Menyuni ko'rish uchun 3, Sotib olish uchun 5, admin sifatida kirish uchun 6(chiqish uchun 4): ")

    if tekshiruv == "1":
        ism = input("Ismingizni kiriting: ")
        parol = input("Parolni kiriting: ")

        try:
            with open(ism + ".txt", "r") as f:
                malumot = f.read()

            if parol in malumot:
                print("\nProfil ma'lumotlari:")
                print(malumot)
            else:
                print("Parol xato!")

        except:
            print("Bunday foydalanuvchi mavjud emas. Avval ro'yxatdan o'ting!")

    elif tekshiruv == "2":
        ism = input("Ismingizni kiriting: ")
        parol = input("Parolni kiriting: ")

        with open(ism + ".txt", "w") as f:
            f.write(f"Ism: {ism}\nParol: {parol}")

        print("Ro'yxatdan o'tdingiz!")

    elif tekshiruv == "5":
        o=5000
        n=3000
        l=4000
        a=int(input("Nechta olma olmoqchisiz? "))
        b=int(input("Nechta nok olmoqchisiz? "))
        c=int(input("Nechta limon olmoqchisiz? "))
        narx=o*a+b*n+c*l
        print("Siz ", narx,  " so'mlik harid amalga oshirdingiz!")
    elif tekshiruv == "4":
        print("Dastur tugadi.")
        break
    elif tekshiruv == "3":
        mahsulot = input("Qaysi mahsulot haqida ma'lumot olishni xohlaysiz?: ")
        with open("Market.txt") as market:
            qatorlar = market.readlines()
            for qator in qatorlar:
                if mahsulot.lower() in qator.lower():
                    print("Topildi: ", qator)
            break
    elif tekshiruv == "6":
        admin_parol = input("Admin parolini kiriting: ")
        if admin_parol == "admin123":
            print("Admin paneliga xush kelibsiz!")
            yangimahsulot = input("Yangi mahsulot nomini kiriting: ")
            with open("Market.txt", "a") as market:
                market.write("\n" + yangimahsulot)
                print("Mahsulot marketga qo'shildi.")
        else:
            print("Noto'g'ri admin paroli!")
    else:
        print("Noto'g'ri tanlov! Mavjud buyruqlardan birini tanlang.")