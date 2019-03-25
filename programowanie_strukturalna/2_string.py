text = "Anna, paweł, JulIA"
lista = text.split(", ")
print(text)
print(lista)
print(type(lista))

imie1 = lista[0]
print(imie1) #Anna
print("Twoje imie:",imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)
