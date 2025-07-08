# OUIGLASS FACTPRO V4 By BRIAN
# Logiciel de gestion pour S.A.S Normandie Vitrages

# Importation des modules nécessaires
import sys
# Importation des modules
from modules import clients, factures, services, stock, analytics

def page_lancement():
    print("OUIGLASS FACTPRO V4 By BRIAN")
    print("Chargement des modules...")
    print("Bienvenue dans le logiciel de gestion hypermoderne.")

def page_connexion():
    print("Page de connexion")
    print("Veuillez entrer votre code à 4 chiffres :")
    code = input("Code : ")
    if code == "7627":
        print("Bienvenue Nicolas (Patron)")
    elif code == "1928":
        print("Bienvenue Aurélie (Secrétaire)")
    elif code == "0205":
        print("Bienvenue Brian (Ouvrier)")
    elif code == "2819":
        print("Bienvenue Mickael (Ouvrier)")
    else:
        print("Code incorrect")

def main():
    print("Bienvenue dans OUIGLASS FACTPRO V4 By BRIAN")
    print("Chargement en cours...")
    page_lancement()
    page_connexion()

if __name__ == "__main__":
    main()
