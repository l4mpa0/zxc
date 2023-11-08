a = int(input('Wpisz pierwszą liczbę: '))
b = int(input('Wpisz drugą liczbę: '))

x = input('Wybierz operację (+, -, *, /, //, %, **): ')

def calculator(a, b, operator):
    wynik = None  
    if operator == '+':
        wynik = a + b
    elif operator == '-':
        wynik = a - b
    elif operator == '*':
        wynik = a * b
    elif operator == '/':
        if b == 0:
            print('Nie można dzielić przez zero.')
            return
        wynik = a / b
    elif operator == '//':
      if b == 0:
          print('Nie można dzielić przez zero.')
          return
      wynik = a // b
    elif operator == '%':
        if b == 0:
            print('Nie można dzielić przez zero.')
            return
        wynik = a % b
    elif operator == '**':
      wynik = a ** b
  
    else:
        print('Nieprawidłowa operacja. Wybierz spośród: +, -, *, /, //, %, **')
        return

    print(f'{a} {operator} {b} = {wynik}')

calculator(a, b, x)
s = input("Czy chcesz kontynuować? (TAK/NIE): ").upper()
while s == "T" or s == "TAK":
    a = int(input('Wpisz pierwszą liczbę: '))
    b = int(input('Wpisz drugą liczbę: '))
    x = input('Wybierz operację (+, -, *, /, //, %, **): ')
    calculator(a, b, x)
    s = input("Czy chcesz kontynuować? (TAK/NIE): ").upper()

print("Poproszę szóstkę :)")
