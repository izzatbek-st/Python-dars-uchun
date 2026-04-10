def kabisa_yili(yil):
    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)

def oy_kunlari(oy, yil):
    if oy in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if oy in [4, 6, 9, 11]:
        return 30
    if oy == 2:
        return 29 if kabisa_yili(yil) else 28
    return 0

def jami_kun(y, o, k):
    kunlar = 0
    for yil in range(1, y):
        kunlar += 366 if kabisa_yili(yil) else 365
        
    for oy in range(1, o):
        kunlar += oy_kunlari(oy, y)
        
    kunlar += k
    return kunlar

def main():
    hozirgi = input("Hozirgi sana (yil oy kun): ").split()
    tugilgan = input("Tug'ilgan sana (yil oy kun): ").split()
    
    y2, o2, k2 = int(hozirgi[0]), int(hozirgi[1]), int(hozirgi[2])
    y1, o1, k1 = int(tugilgan[0]), int(tugilgan[1]), int(tugilgan[2])
    
    natija = jami_kun(y2, o2, k2) - jami_kun(y1, o1, k1)
    
    print(natija)

main()