from tkinter import image_types


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1==n2:
    print('Eles são Iguais')
else:
    if n1>n2:
        print('São diferentes: %d'%n1)
    else:
        print('São diferentes: %d'%n2)
