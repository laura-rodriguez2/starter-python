nombre = int(input ("Entrez un nombre de lettres : "))

with open("data.txt", "r") as f:
    text = f.read()
    text = text.replace(",", "").replace(";", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "")
    words = text.split()
    count = 0

    for i in words:
        if len(i) == nombre:
            count = count +1

print("Mots avec ce nombre de lettres :",count)