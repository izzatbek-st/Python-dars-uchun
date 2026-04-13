def son_ol():
    son = input("son kiriting: ")
    return int(son)

def hisobla():
    a = son_ol()
    
    for i in range(1,a+1):
        for b in range(1, 10):
            print(i, "x", b, "=", i*b)


def main():
    hisobla()