while True:
    try:
        a = int(input("1-xonali son kiriting: "))
        b = int(input("Yana 1-xonali son kiriting: "))

        if a >= 10 or b >= 10:
            print("Xato! Faqat 1-xonali son kiriting.")
            continue

        print("Natija:", a * b)

    except:
        print("Xato! Iltimos faqat son kiriting.")
