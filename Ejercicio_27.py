#ejercicio 27

letra = input("Introduce una letra: ")

if len(letra) == 1:
    if letra.isalpha():
        if letra.isupper():
            print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
elif letra.isdigit():
    print("El valor introducido es un número")
else:
    print("¿?")

