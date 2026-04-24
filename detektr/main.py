def get_text():
    text = input("Matn kiriting: ")
    return text

def tekshir():
    matn = get_text()
    with open("badwords.txt", "r") as file:
        badwords = file.read().split("\n")
    for word in badwords:
        if word in matn.lower():
            matn = matn.replace(word, "*" * len(word))
    print(matn)

def main():
    tekshir()



main()