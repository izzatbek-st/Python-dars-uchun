try:
    son = int(input("1 xonali son kiriting: "))

    if son >= 10:
        raise ValueError("1 xonali son emas")

    print("To‘g‘ri son:", son)

except ValueError:
    print("Xato! 1 xonali son kiritish kerak.")
