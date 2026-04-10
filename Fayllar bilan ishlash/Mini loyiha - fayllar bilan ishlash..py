from PIL import Image
import PyPDF2

def fayl_och(nomi):
    if nomi.endswith(".txt"):
        with open(nomi, "r", encoding="utf-8") as f:
            print(f.read())

    elif nomi.endswith(".pdf"):
        with open(nomi, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            print(reader.pages[0].extract_text())

    elif nomi.endswith(".jpg") or nomi.endswith(".png"):
        img = Image.open(nomi)
        img.show()

    else:
        print("Bu fayl turi qo‘llab-quvvatlanmaydi")

# ishga tushirish
fayl_och("test.pdf")
