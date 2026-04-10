f = open("Text Document")
print(f.read())

with open("Text Document") as f:
    print(f.read())







with open("Text Document", "a") as f:
    a = f.write(" qo'shildi a bilan")
print(a)

with open("Text Document", "a") as f:
    f.write(" qo'shildi a bilan")
    
with open("Text Document", "w") as f:
    f.write(" qayta yozildi w bilan")

with open("Text Document", "r") as f:
    print(f.read())
