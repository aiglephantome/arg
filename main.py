
import random
import string
import webbrowser

def generer_mot_de_passe(n):
    caracteres = string.ascii_uppercase + string.digits
    mot_de_passe = ""

    for _ in range(n):
        caractere = random.choice(caracteres)
        mot_de_passe += caractere

    return mot_de_passe

longueur_mot_de_passe = int(input("Quelle est la longueur souhaitée pour le mot de passe? "))
nombre_mot_de_passe = int(input("Combien de mots de passe voulez-vous générer? "))

for _ in range(nombre_mot_de_passe):
    mot_de_passe = generer_mot_de_passe(longueur_mot_de_passe)
    lien = "https://www.fortnite.com/vbuckscard?code=" + mot_de_passe
    print(lien)
    webbrowser.open(lien)