txt = input("Entrez un texte : ")

# permet de créer et d'écrire un contenu dans output.txt
with open("./output.txt", "a") as file:
	file.write(txt)
	file.write('\n')

# lit et écrit le contenu de output.txt
with open("./output.txt") as file:
	print (file.read())
