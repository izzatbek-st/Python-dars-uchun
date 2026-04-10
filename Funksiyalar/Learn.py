def kvadratlar(sonlar):
    natija = []
    for x in sonlar:
        natija.append(x * x)
    return natija


numbers = [1, 2, 3, 4, 5]
javob = kvadratlar(numbers)

print(javob)