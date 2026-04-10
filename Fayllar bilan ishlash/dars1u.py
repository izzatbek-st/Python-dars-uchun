from time import sleep
from datetime import datetime
from Funksiyalar import salom

def showtime(count=5):
    for i in range(5, -1, -1):
        print(i)
        sleep(1)
    print('booooooom')

showtime()
salom()