# 3.4
while True:
    text = input("Podaj liczbę (stop kończy): ").strip()
    if text == "stop":
        break
    try:
        x = float(text)
    except ValueError:
        print("To nie jest liczba:", text)
        continue
    print(x, x ** 3)
