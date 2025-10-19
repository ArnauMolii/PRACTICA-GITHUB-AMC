#ejeercicio 31

frase = "A quién madruga Dios ayuda"
palabras = ["madruga", "Dios", "dios"]

for palabra in palabras:
    if palabra in frase:
        indice = frase.index(palabra)
        print(f"La palabra está en la frase y está en el índice {indice}")
else:
    print(f"La palabra no está en la frase")
