# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
(cities) = ("Barcelona", "Madrid", "Sevilla", "Valencia", "Bilbao")
print(cities[1])
print(cities[-2])

# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
(numbers) = (1, 2, 3, 4, 5, 3, 6, 3, 3, 7, 3)
print(numbers.count(3))

# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ordenar_tupla(tupla):
    return tuple(sorted(tupla))
ordenada = ordenar_tupla((5, 2, 9, 1, 5, 6))
print(ordenada)
