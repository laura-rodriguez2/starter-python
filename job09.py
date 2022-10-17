hauteur = int(input("Entrez la hauteur : "))
x = 1
y = hauteur
while x <= hauteur:

	for i in range (0,hauteur-x):
		print (" ", end = '')
	print ("/", end = '')

	for j in range (0,hauteur-y):
		if hauteur-x == 0:
			print ("_", end = '')
		else:
			print (" ", end = '')

	print ("\\")
	x += 1
	y -= 2
