def yourage(age):
    new_age = age + 50
    return new_age

age = float(input("Wpisz swoj wiek "))


if age <= 150:
    print(yourage(age))
else:
    print("Chyba sobie zartujesz")
