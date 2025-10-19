#ejercicio 26

letra = input("Introduce una letra: ")

if len(letra) == 1 and letra.isalpha():
    if letra.isupper():
        print("La letra es mayúscula")
if letra.islower():
    print("La letra es minúscula")
else:
    print("¿?")
