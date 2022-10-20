file = open("data.txt", "rt")

data = file.read()

words = data.split()

print('Nombre de mots dans ce fichier :', len(words))