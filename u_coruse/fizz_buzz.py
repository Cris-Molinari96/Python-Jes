# L'esercizio ci chiede di verificare che i numeri da 1 a 100 sono divisibili per 3, 5 o entrambi e chiaro nel codice
# che sè il numero n è divisibile per 3, 5 o entrambi accade qualcosa.
def main():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

main()