

def decompositionDate(arg_date):
    
    date_obj = arg_date.split("-")
    annee = int(date_obj[0])
    mois = int(date_obj[1])
    jour = int(date_obj[2])
    heure = 0
    minute = 0
    seconde = 0

    return annee, mois, jour, heure, minute, seconde


def decompositionDateComplete(arg_date):
    
    date_obj = arg_date.split(":")
    annee, mois, jour, heure, minute, seconde = decompositionDate(date_obj[0])
    heure = 0
    minute = 0
    seconde = 0

    if len(date_obj) == 1:

        annee, mois, jour, heure, minute, seconde = decompositionDate(date_obj[0])

    else:

        if date_obj[1] != "":
            heure = int(date_obj[1])

        if date_obj[2] != "":
            minute = int(date_obj[2])

        if date_obj[3] != "":
            seconde = int(date_obj[3])

    return annee, mois, jour, heure, minute, seconde


def verifieBissextile(annee):
    
    bissextile = False

    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        bissextile = True

    return bissextile


def verifieJourAnneeBissextile(annee, mois, jour):

    dico_annee_biss = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    mois2 = mois

    for i in dico_annee_biss.keys():
        
        if i == mois2 and jour > dico_annee_biss[i]:
            while (jour > dico_annee_biss[i]):

                jour = jour - dico_annee_biss[i]

                i += 1

                if i == 13:
                    i = 1
                elif i > 13:
                    i = i - 12

                mois2 = i
        elif i == mois2 and jour == 0:

            jour = dico_annee_biss[i - 1]
            i = i - 1

            if i == 0:
                i = 12
                annee = annee - 1

            mois2 = i

    mois = mois2
    
    return annee, mois, jour


def verifieJourAnneeNonBissextile(annee, mois, jour):

    
    dico_annee_non_biss = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    mois2 = mois

    for i in dico_annee_non_biss.keys():

        if i == mois2 and jour > dico_annee_non_biss[i]:

            while jour > dico_annee_non_biss[i]:

                jour = jour - dico_annee_non_biss[i]

                i += 1

                if i == 13:
                    i = 1
                elif i > 13:
                    i = i - 12

                mois2 = i

            jour = jour
            
        elif i == mois2 and jour == 0:

            i = i - 1
            
            if i == 0:
                i = 12
                annee = annee - 1
                
            jour = dico_annee_non_biss[i]
            mois2 = i
             
    mois = mois2
    
    return annee, mois, jour


def rectifieJour(annee, mois, jour):

    bissextile = verifieBissextile(annee)
    
    if bissextile:

        nb_annee= jour //366
        jour = jour % 366
        annee = annee + nb_annee
    else:

        nb_annee = jour // 365
        jour = jour % 365
        annee = annee + nb_annee

    bissextile2 = verifieBissextile(annee)
    
    if jour == 0:
        
        if bissextile2:
            
           annee, mois, jour = verifieJourAnneeBissextile(annee, mois, jour)
           
        else:
            
           annee, mois, jour = verifieJourAnneeNonBissextile(annee, mois, jour)
            

    if mois in [1, 3, 5, 7, 8, 10, 12]:

        if jour > 31:
            if bissextile2:
                annee, mois, jour = verifieJourAnneeBissextile(annee, mois, jour)
            else :

                annee, mois, jour = verifieJourAnneeNonBissextile(annee, mois, jour)
                
                
    if mois == 2 and bissextile2:
        if jour > 29:

            annee, mois, jour = verifieJourAnneeBissextile(annee, mois, jour)

    if mois == 2 and not bissextile2:
        if jour > 28:

            annee, mois, jour = verifieJourAnneeNonBissextile(annee, mois, jour)

    if mois in [4, 6, 9, 11]:

        if jour > 30:
            if bissextile2:
                
                annee, mois, jour = verifieJourAnneeBissextile(annee, mois, jour)
                
            else:

                annee, mois, jour = verifieJourAnneeNonBissextile(annee, mois, jour)
                
                
    return annee, mois, jour


def rectifieHeure(annee, mois, jour, heure):
    
    if heure >= 24:
        jour = jour + (heure//24)

        heure = heure % 24

    annee, mois, jour = rectifieJour(annee, mois, jour)
    
    return annee, mois, jour, heure


def rectifieMinute(annee, mois, jour, heure, minute):
    
    if minute >= 60:
        heure = heure + (minute // 60)
        minute = minute % 60

    annee, mois, jour, heure = rectifieHeure(annee, mois, jour, heure)
    
    return annee, mois, jour, heure, minute


def calculAdditionTemps(arg_date, nb_jours=0, nb_heures=0, nb_minutes=0, nb_secondes=0):
    
    annee, mois, jour, heure, minute, seconde = decompositionDateComplete(arg_date)

    ##### ADDITION DU JOUR

    if nb_jours != 0:
        jour = jour + nb_jours

        annee, mois, jour = rectifieJour(annee, mois, jour)

    ##### ADDITION DE L'HEURE

    if nb_heures != 0:
        heure = heure + nb_heures

        annee, mois, jour, heure = rectifieHeure(annee, mois, jour, heure)

    ##### ADDITION DE MINUTES

    if nb_minutes != 0:
        minute = minute + nb_minutes

        annee, mois, jour, heure, minute = rectifieMinute(annee, mois, jour, heure, minute)

    ##### ADDITION DE SECONDES

    if nb_secondes != 0:

        seconde = seconde + nb_secondes

        if seconde >= 60:
            
            minute = minute + (seconde // 60)
            seconde = seconde % 60
            
            annee, mois, jour, heure, minute = rectifieMinute(annee, mois, jour, heure, minute)
            

    return annee, mois, jour, heure, minute, seconde


def calculSoustrationTemps(arg_date,  nb_heures=0, nb_minutes=0):

    annee, mois, jour, heure, minute, seconde = decompositionDateComplete(arg_date)


    ##### SOUSTRACTION D'HEURES

    if nb_heures != 0:
        heure = (heure + nb_heures)
        if heure < 0:

            jour -= 1
            heure = 24 + heure

        annee, mois, jour, heure = rectifieHeure(annee, mois, jour, heure)

    ##### SOUSTRACTION DE MINUTES

    if nb_minutes != 0:
        minute = (minute + nb_minutes)
        if minute <0:
            heure -= 1
            minute = 60 + minute

        annee, mois, jour, heure, minute = rectifieMinute(annee, mois, jour, heure, minute)



    return annee, mois, jour, heure, minute, seconde


#def convertitFuseau(arg_date, new_fuseau):
    


def formatDateHeure(annee, mois, jour, heure=0, minute=0, seconde=0):
    
    result = f"La date recherchée est : {annee} - {mois} - {jour} : {heure} : {minute} : {seconde} "
    
    return result
