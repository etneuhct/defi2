

def decompositionDate(arg_date):

    date_obj = arg_date.split("-")
    annee = int(date_obj[0])
    mois = int(date_obj[1])
    jour = int(date_obj[2])
    heure=0
    minute=0
    seconde=0

    return annee, mois, jour, heure, minute, seconde


def decompositionDateComplete(arg_date):

    date_obj = arg_date.split(":")
    annee, mois, jour, heure, minute, seconde = decompositionDate(date_obj[0])
    heure = 0
    minute = 0
    seconde = 0

    if len(date_obj) == 1:

        annee, mois, jour, heure, minute, seconde = decompositionDate(date_obj[0])

    else :

        if date_obj[1] != "":

            heure = int(date_obj[1])

        if date_obj[2] != "":
            minute = int(date_obj[2])

        if date_obj[3] != "":
            seconde = int(date_obj[3])

    return annee, mois, jour, heure, minute, seconde


def checkBissextile(annee):

    bissextile= False

    if annee % 4 ==0 and annee % 100 !=0 or annee % 400 ==0:

        bissextile=True

    return bissextile



def checkJour(annee, mois, jour) :


    if mois in [1,3,5,7,8,10,12] and jour >= 31:

            mois = mois + 1

            if mois == 13:

                annee = annee + 1
                mois = 1

            if jour == 31:
                jour = 1

            else:

                jour = jour - 30

    if mois == 2 and checkBissextile(annee) and jour >= 29: #ANNEE BISSEXTILE

            mois = mois +1

            if jour == 29:
                jour = 1

            else:

                jour = jour - 28


    if mois == 2 and not checkBissextile(annee) and jour >= 28:

            mois = mois + 1
            if jour == 28:
                jour = 1

            else:

                jour = jour - 27

    if mois in [4, 6, 9, 11] and jour >= 30:

            mois = mois +1
            if jour == 30:
                jour = 1

            else:

                jour = jour - 29


    return annee, mois, jour


def checkHeure(annee, mois, jour, heure):

    if heure >= 24:
        jour = jour + 1

        heure = heure - 24

        annee, mois, jour = checkJour(annee, mois, jour)

    return annee, mois, jour, heure


def checkMinute(annee, mois, jour, heure, minute):

    if minute >= 60:
        minute = minute - 60
        heure = heure+ 1

        annee, mois, jour, heure = checkHeure(annee, mois, jour, heure)

    return annee, mois, jour, heure, minute



def CalculTemps(arg_date, nb_jours =0, nb_heures=0, nb_minutes=0, nb_secondes=0) :



    annee, mois, jour, heure, minute, seconde = decompositionDateComplete(arg_date)

    ##### ADDITION DU JOUR

    if nb_jours != 0 :
        jour = jour + nb_jours

        annee, mois, jour = checkJour(annee, mois, jour)


    ##### ADDITION DE L'HEURE

    if nb_heures != 0 :

        heure =heure + nb_heures

        annee, mois, jour, heure = checkHeure(annee, mois, jour, heure)


    ##### ADDITION DE MINUTES

    if nb_minutes != 0 :
        minute = minute + nb_minutes

        annee, mois, jour, heure, minute = checkMinute(annee, mois, jour, heure, minute)


    ##### ADDITION DE SECONDES

    if nb_secondes != 0 :

        seconde = seconde + nb_secondes

        if seconde >= 60 :

            seconde = seconde -60
            minute = minute + 1

            annee, mois, jour, heure, minute = checkMinute(annee, mois, jour, heure, minute)


    return   annee, mois, jour, heure, minute, seconde



def formatDateHeure(annee, mois, jour, heure=0, minute=0, seconde=0) :

    print("La date recherchée est : ",annee,"-",mois,"-",jour,":",heure,":",minute,":",seconde)







