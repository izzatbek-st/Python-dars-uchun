def get_number():
    number = input("Sekundni yozing: ")
    while not number.isdigit():
        number = input("Sekundni yozing: ")
    return int(number)

def hisobla():
    sekund = get_number()
    h = sekund // 3600
    m = (sekund - h*3600) // 60
    s = sekund - (h*3600+m*60)
    print(f"{h} soat, {m} daqiqa, {s} soniya")

def main():
    hisobla()


main()