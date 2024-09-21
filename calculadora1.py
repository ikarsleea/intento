# COMMENT
print("Bienvenid@, Para + y - escriba 1. Para Multiplicar y dividir escriba 2")
i = int(input(""))
if i == 1: 
    import Suma
else:
    import multiplicar
print("Para continuar haciendo operatoria marque 3, para salir, marque 4")
i = int(input(""))
if i == 3:
    import calculadora1
    calculadora1
else:
    print("Bye Bye")
