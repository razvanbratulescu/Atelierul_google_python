# print("mesaj nr {}".format(1))
# raspuns_utilizator = input("care este numele tau: ")
# print(raspuns_utilizator)
#
# def functia_mea(param_1):
#     pass

# def suma(a,b) -> (int, int):
#     """
#     :param a: primul numar
#     :param b: al doile numar
#     :return: suma, diferenta
#     """
#     return a + b, a - b
# #cand ajunge la return se iese din functie
#
# suma_mea, diferenta = suma(1 , 2)
# print(suma_mea, diferenta)

# def my_function(*param_1):
#     print(type(param_1))
#     return param_1
# print(my_function("string", "strin1", "string2"))

# def suma_nr_infinite(param1, param2, *var):
#     sum = 0
#     for item in var:
#         suma += item
#     return suma
#
# print(suma_nr_infinite(1 ,2,3,4,5,6,7))
#
# def catalog(*args, **kwargs):#tuplu si dictionar
#     print(type(kwargs))
#     return args, kwargs
#
# print(catalog(1,2, nume="ION", prenume="Vasile", varsta="12"))
a, b = 10, 20
min = a if a<b else b
print(min)

lista_produse = ["ciocolata", "mere", "apa", "cuvant"]
# lista_noua = []
# for x in lista_produse:
#     if "a" in x:
#         lista_noua.append(x)

#lista_noua = [x for x in lista_produse if "a" in x]
# lista_noua = [x if "a" in x else "b" for x in lista_produse]
#
#
# print(lista_noua)

# min = None
# if min:= a < b:
#     print(min)
#     min = a
# else:
#     min = b
