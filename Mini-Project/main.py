cost = int(input("ต้นทุน: "))
profit = int(input("กำไร(%) "))

cal = (cost/(100-profit))*100
print("You should sall %.2f bath" % cal)