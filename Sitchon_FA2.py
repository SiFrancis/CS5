import math

rad = int(input("Enter Diameter: "))/2
area = 3.14 * (rad ** 2)
price = int(input("Enter Price: "))
print(str(price/area) + " per sq inch")
