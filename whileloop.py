password = ''
while password != 'python123':
    password = input("Wpisz password ")
    if password == 'python123':
        print("Zalogowales sie!")
    else:
        print("Zle haslo. Sproboj ponownie")
