# Branching Statement
# If
# If .. Else
# Elif Ladder
# Nested If

a = 5
if a == 5:
    print("Equal")
elif a >= 4:
    print("Greater then 5")
else:
    print("Not Equal")
print("\n")
price = 50
normalPrice = 60
fanceyPenPrice = 100
HandPrice = int(input("Enetr your price : "))
if HandPrice >= price:
    if HandPrice >= fanceyPenPrice:
        print("You can buy Two pens..")
    else:
        print("You can buy One pens ")
else:
    print("Insufficince amount...")