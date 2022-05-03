variabile = input("Introdu un numar: ")
my_int = None
try:
    este_intreg = int(variabile)
    if my_int is None:
        raise ValueError
# except ValueError as e:
#     print('eraoarea de valoare', e)
except Exception as e:
    print("a aparut o eroare", e)

finally:
    print("se ruleaza oricum")
