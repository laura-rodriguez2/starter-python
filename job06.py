valeur1 = int(input("1ère valeur : "))
valeur2 = int(input("2ème valeur : "))

if valeur1 == valeur2:
    print("Les deux valeurs sont égales")
elif valeur1 < valeur2:
    for i in range(valeur1 +1 , valeur2):
        print(i)
else:
    for i in range(valeur1 -1, valeur2, -1):
        print(i)