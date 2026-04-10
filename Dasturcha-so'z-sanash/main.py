def get_text():
    matn = input("Matnni kiriting: ")
    return matn

def file_save(text, filename="matn.txt"):
    with open(filename, "w") as f:
          f.write(text)
    print("Fayl saqlandi!")

def main():
    matn = get_text()
    words_count = len(matn.split())
    print(f"Siz kiritgan matnda {words_count} ta so'z bor.")
    file_save(matn)
    print("="*30)

main()