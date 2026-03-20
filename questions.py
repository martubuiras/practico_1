import random
categorias = {
        "programacion": ["python", "programa", "variable", "funcion"],
        "elementos": ["cadena", "entero", "lista", "bucle"]
    
}

print ("Categorias disponibles:")
for categoria in categorias:
    print (categoria)

elegida = input ("Elija una categoria: ")
palabras = random.sample(categorias[elegida], len(categorias[elegida]))
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

for word in palabras:

    guessed = []
    attempts = 6
    puntaje = 0

    print ("Nueva ronda")
    print()

    while attempts > 0:
     # Mostrar progreso: letras adivinadas y guiones para las que faltan
     progress = ""
     for letter in word:
         if letter in guessed:
            progress += letter + " "
         else:
            progress += "_ "
     print(progress)
     #  Verificar si el jugador ya adivinó la palabra completa
        
     if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        print (f"Tu puntaje final es: {puntaje}")
        break

     print(f"Intentos restantes: {attempts}")
     print(f"Letras usadas: {', '.join(guessed)}")

     letter = input("Ingresá una letra: ")

     if len(letter) != 1 or not (
         (letter >= "a" and letter <= "z") or
         (letter >= "A" and letter <= "Z")
     ):
         print ("Entrada no valida")
         print ()
         continue
  
     if letter in guessed:
          print("Ya usaste esa letra.")
     elif letter in word:
         guessed.append(letter)
         print("¡Bien! Esa letra está en la palabra.")
     else:
         guessed.append(letter)
         attempts -= 1
         puntaje -= 1 
         print("Esa letra no está en la palabra.")
     print()

    else:
     puntaje = 0
     print(f"¡Perdiste! La palabra era: {word}")
     print (f"Tu puntaje final es: {puntaje}")