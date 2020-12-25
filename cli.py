import re
from gestionTemps import CalculTemps, formatDateHeure, obtenir_valeur_initiale

def obtenir_format_valeur_a_ajouter():

    while True:

        format_valeur = input("Entrer \n1 Jour\n2 Heure\n3 Minute\n4 Seconde")

        try:
            format_valeur = int(format_valeur)
        except ValueError:
            print("Veuillez selectionner une des options proposées")
            continue

        if format_valeur not in range(1, 5):
            print("Veuillez selectionner un format valide")
            continue

        return format_valeur


def obtenir_valeur_a_ajouter():

    while True:
        valeur = input("Entrer la valeur à ajouter à la date initiale")
        try:
            valeur = int(valeur)
        except ValueError:
            print("Veuiller rentrer une valeur numérique")
            continue
        return valeur


def obtenir_valeur_initiale():
    format_court = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format_complet = '[0-9]{4}-[0-9]{2}-[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{2}'
    while True:
        date_initiale = input("Inserer la date initiale")
        result = 0 if re.search(format_court, date_initiale) else 1 if re.search(format_complet, date_initiale) else 2

        if result == 2:
            print("Veuillez rentrer une date au format valide yyyy-MM-jj:hh:mm:ss ou yyyy-MM-jj")
            continue

        return date_initiale, result


if __name__ == '__main__':

    d_i, format_result = obtenir_valeur_initiale()
    ajouter_nouvelle_valeur = True
    valeurs = {}

    while ajouter_nouvelle_valeur:

        f_v = obtenir_format_valeur_a_ajouter()
        v = obtenir_valeur_a_ajouter()

        if f_v not in valeurs:
            valeurs[f_v] = v
        else:
            valeurs[f_v] = valeurs[f_v] + v

        annee, mois, jour, heure, minute, seconde = CalculTemps(d_i, v)
        print(formatDateHeure(annee, mois, jour, heure, minute, seconde))

        ajouter_nouvelle_valeur = input("Souhaitez vous ajouter une nouvelle valeur au calcul ? (o/n)").lower() == 'o'






















