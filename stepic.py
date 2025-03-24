##%%
age = 22
member = True
deposit = 15

if age > 18:
    if member:
        if deposit > 0:
            if deposit >= 75:
                print("Цена билета 0")
                print('Сняты средства с депозита в размере 75р')
                deposit -= 75
            else:
                print(f"Цена билета {75 - deposit}")
                print('Ваш депозит полностью потрачен')
                deposit = 0
        else:
            print("Цена билета 75")
    else:
        print("Цена билета 100")
else:
    if member:
        if deposit > 0:
            if deposit >= 25:
                print("Цена билета 0")
                print('Сняты средства с депозита в размере 25р')
                deposit -= 75
            else:
                print(f"Цена билета {25 - deposit}")
                print('Ваш депозит полностью потрачен')
                deposit = 0
        else:
            print("Цена билета 25")
    else:
        print("Цена билета 50")


