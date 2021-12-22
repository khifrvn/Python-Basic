try:
    age = int(input("Age : "))
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Zero Error")


# ============= COMMENT ============
"""
"""
# -----> this is comment

while True:
    try:
        angka = int(input("Harga barang: "))
        break
    except ValueError:
        print("Error value 'barang'")
    except ZeroDivisionError:
        print("Error Zero")

print('Harga Barang :', angka)