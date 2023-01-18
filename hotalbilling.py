print("welcom the Ajith Hotal")
x = int(input("select the manu\n1.Idely\n2.vadai\n3.Dhose\n4.poori"))


if x == 1:
     a = int(input("Enter the quantity :"))
     price = a*10
     print("The price =", price)
elif x == 2:
    a = int(input("Enter the quantity :"))
    price = a*8
    print("The price =", price)
elif x == 3:
    a = int(input("Enter the quantity :"))
    price = a*15
    print("The price =", price)
elif x == 4:
     a = int(input("Enter the quantity :"))
     price = a*30
     print("The price =", price)
else:
    print("No option")


