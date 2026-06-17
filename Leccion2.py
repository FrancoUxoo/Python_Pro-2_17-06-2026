# Python_Pro-2_17-06-2026

print ("Bienvenido al Diccionario de Memes")
print("Escribe una palabra en MAYÚSCULAS para conocer su significado.\n ")

meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo raro o embarazoso",
    "ROFL":"Una respuesta a una broma",
    "SHEESH":"Ligera desaprobación",
    "CREEPY":"Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo o enojado"
}

for i in range(5):
    word = input("\nEscribe una palabra que no entiendas: ")

    if word in meme_dict:
        print("Significado:", meme_dict[word])
    else:
        print("Lo siento, esa palabra no está en el diccionario.")
