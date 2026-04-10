def count_days(sana):
    days = (int(sana[0])*365+(int(sana[0])//4)) + (int(sana[1])*30) + int(sana[2])
    return days


def from_one_now():
    now = input("Hozirgi sanani kiriting: ")
    return now.split()

def from_one_born():
    born = input("Tug'ilgan sanani kiriting: ")
    return born.split()

def main():
    until_now = from_one_now()
    until_born = from_one_born()
    counted_now = count_days(until_now)
    counted_born = count_days(until_born)
    end = counted_now - counted_born
    print(end)

main()