lista = ["uva", "melão", "maçã", "banana", "acerola", "abacaxi"]

while True:
    menu = int(input("""
    escolha uma opção:
    1 - excluir a ultima fruta
    2 - escolher qual fruta excluir 
    0 - sair
"""))
    
    match menu:
        case 1:
            lista.pop()
        case 2:
            print(lista)
            posicao = int(input("qual posição da fruta você quer apagar:"))
            lista.pop(posicao -1)
        case 0:
            break
        case _:
            print("operação invalida")


