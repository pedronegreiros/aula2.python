lista = ["uva", "melão", "maçã", "banana", "acerola", "abacaxi"]

print("uva = 0")
print("melão = 1")
print("maçã = 2")
print("banana = 3")
print("acerola = 4")
print("abacaxi = 5")

fruta = int(input("qual numero da fruta que deseja excluir?: "))


lista.pop(fruta)

print (lista)
