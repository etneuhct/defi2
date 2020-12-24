from datetime import datetime

def decompositionDate(arg_date) :


    #Liste_Mois= ["Janvier", "Fevrier", "Mars","Avril","Mai", "Juin", "Juillet", "Aout","Septembre","Octobre",
                # "Novembre", "Decembre"]

    date_obj = arg_date.split("-")
    annee = int(date_obj[0])
    mois = int(date_obj[1])
    jour = int(date_obj[2])
   # vrai_mois = 0


    #for i in range(1,12):

        #if mois == Liste_Mois[i] :

            #vrai_mois = i


    return annee, mois, jour


def decompositionDateComplete(arg_date) :


    date_obj = arg_date.split(":")

    annee, mois, jour = decompositionDate(date_obj[0])
    heure = 0
    minute = 0
    seconde = 0
    if date_obj[1]!="" :

        heure = int(date_obj[1])

    if date_obj[2] != "":
        minute = int(date_obj[2])

    if date_obj[3] != "":
        seconde = int(date_obj[3])

    return annee, mois, jour, heure, minute, seconde


def checkJour(mois, jour) :

    if mois in [1,3,5,7,8,10,12] and jour >= 31 :

            mois =+ 1
            jour = jour - 31
            if mois == 12:
                mois = 1
                annee = + 1

    if mois == 2 and (annee==2020 or annee==2020 +4) and jour>=29 : #ANNEE BISSEXTILE

            mois = +1
            jour = jour - 29

            if mois == 12:
                mois = 1
                annee = + 1

    if mois ==2 and (annee==2021 or annee==2022 or annee==2023 ) and jour>=28:

            mois = +1
            jour = jour - 28

            if mois == 12:
               mois = 1
               annee = + 1

    if mois in [4, 6, 9, 11] and jour >= 30 :

            mois = +1
            jour = jour - 30
            if mois == 12:
                mois = 1
                annee = + 1

    return mois, jour


def CalculTemps(arg_date, nb_jours =0, nb_heures=0, nb_minutes=0, nb_secondes=0) :


    annee, mois, jour, heure, minute, seconde = decompositionDateComplete(arg_date)

    ##### ADDITION DU JOUR

    if nb_jours != 0 :
        jour =+ nb_jours

        mois, jour =checkJour(mois, jour)


    ##### ADDITION DE L'HEURE

    if nb_heures != 0 :

        heure =+ nb_heures

        if heure >= 24 :

            jour =+ 1

            heure = heure -24

            mois, jour = checkJour(mois, jour)


    ##### ADDITION DE MINUTES

    if nb_minutes != 0 :
        minute =+ nb_minutes

        if minute >= 60 :

            minute = minute -60
            heure =+ 1

            if heure >= 24:

                jour = + 1

                heure = heure - 24

                mois, jour = checkJour(mois, jour)


    ##### ADDITION DE SECONDES

    if nb_secondes != 0 :

        seconde =+ nb_secondes

        if seconde >= 60 :

            seconde = seconde -60
            minute =+ 1

            if minute >= 60:

                minute = minute - 60
                heure = + 1

                if heure >= 24:

                    jour = + 1

                    heure = heure - 24

                    mois, jour = checkJour(mois, jour)



    return   annee, mois, jour, heure, minute, seconde









