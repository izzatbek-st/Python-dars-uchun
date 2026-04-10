from datetime import datetime

def get_date():
    print("Sana formati: Yil Oy Kun (masalan: 2000 05 15)")
    sana = input("Sanani kiriting: >> ")
    
    # Foydalanuvchi 3 ta qism (yil, oy, kun) kiritmaguncha so'rayveradi
    while len(sana.split()) != 3:
        print("Xato! Iltimos, sanani ko'rsatilgan formatda kiriting.")
        sana = input("Sanani kiriting: >> ")
        
    return sana.split()

def main():
    # Hozirgi vaqtni olish
    now = datetime.now().date()
    
    # Foydalanuvchidan sanani olish
    date_list = get_date()
    
    try:
        # Kiritilgan sanani date obyektiga o'tkazish
        since = datetime(int(date_list[0]), int(date_list[1]), int(date_list[2])).date()
        
        # Farqni hisoblash (Ayirish belgisi '-' bo'lishi shart)
        diff = now - since
        
        print(f"O'tgan kunlar soni: {abs(diff.days)} kun")
        
    except ValueError:
        print("Xato: Mavjud bo'lmagan sana kiritildi (masalan, 13-oy yoki 32-kun).")

if __name__ == "__main__":
    main()