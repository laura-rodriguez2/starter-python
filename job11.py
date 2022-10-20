file = open("domains.xml", "r")

data = file.read()

occurrences = data.count("domain")

print('Nombre de noms de domaine :', occurrences)