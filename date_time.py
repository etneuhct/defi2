from functools import reduce

from gestionTemps import decompositionDateComplete


class DateFormatInvalid(Exception):
    pass


class DateTime:

    def __init__(self, date_time_string=None, annee=None, mois=None, jour=None, heure=0, minute=0, seconde=0):
        self.mois_31 = [1, 3, 5, 7, 8, 10, 12]
        self.mois_30 = [4, 6, 9, 11]
        self.jours_de_la_semaine = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']

        if date_time_string:
            self.annee, self.mois, self.jour, self.heure, self.minute, self.seconde = decompositionDateComplete(
                date_time_string)
            self.est_coherent()
        elif annee and mois and jour:
            self.annee, self.mois, self.jour, self.heure, self.minute, self.seconde = annee, mois,\
                                                                                      jour, heure, minute, seconde
            self.est_coherent()
        else:
            raise DateFormatInvalid('Information manquante')

    def est_coherent(self):
        if self.mois > 12 or self.mois < 1:
            raise DateFormatInvalid('Le mois doit être une valeur comprise entre 1 et 12')
        if self.jour > 31 or self.jour < 1:
            raise DateFormatInvalid('Le jour doit etre compris entre 1 et 31')
        if (self.jour == 31 and self.mois not in self.mois_31) or (self.jour == 30 and self.mois == 2):
            raise DateFormatInvalid(f'Le mois {self.retourne_valeur_du_mois()} n\'a pas {self.jour} jours.')
        if not self.est_bissextile() and self.mois == 2 and self.jour == 29:
            raise DateFormatInvalid(f'L\'année {self.annee} n\'est pas bissextile. '
                                    f'Le mois {self.retourne_valeur_du_mois()} ne peut pas avoir 29 jours')
        if self.heure > 23:
            raise DateFormatInvalid(f'L\'heure ne peut être superieur à 23')
        return True

    def est_bissextile(self):
        return self.annee % 400 == 0 or (self.annee % 4 == 0 and self.annee % 100 != 0)

    def retourne_valeur_du_mois(self):
        return {
            1: 'Janvier', 2: 'Fevrier', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Decembre'
        }[self.mois]

    def retourne_jour_du_calendrier(self):
        result = []
        valeur_actuelle = -1
        premier_jour_du_mois = self.retourne_premier_jour_du_mois()
        continuer = True
        for i in range(6):
            semaine = []
            if continuer:
                for j in range(7):
                    if valeur_actuelle == -1 and premier_jour_du_mois == j:
                        valeur_actuelle = 0
                    if 0 <= valeur_actuelle < self.nombre_du_jour_dans_le_mois():
                        valeur_actuelle += 1
                    elif self.nombre_du_jour_dans_le_mois() <= valeur_actuelle:
                        valeur_actuelle = 1
                        continuer = False
                    valeur_a_afficher =  f"#{valeur_actuelle}" \
                        if continuer and valeur_actuelle == self.jour else valeur_actuelle
                    jour = '   ' if valeur_a_afficher == -1 \
                        else f' {valeur_a_afficher} ' if len(str(valeur_a_afficher)) < 2 \
                        else f' {valeur_a_afficher}' if len(str(valeur_a_afficher)) < 3 else f'{valeur_a_afficher}'
                    semaine.append(jour)
                result.append(semaine)
        return result

    def retourne_premier_jour_du_mois(self):
        return DateTime(None, self.annee, self.mois, 1).retourne_le_jour_de_la_semaine()

    def retourne_le_jour_de_la_semaine(self):
        secondes_date_actuelle = ConversionDateTime(
            self.annee, self.mois, self.jour, self.heure, self.minute, self.seconde, self.est_bissextile())\
            .convertir_en_secondes()

        secondes_date_reference = ConversionDateTime(
            2020, 12, 23, 0, 0, 0, True
        ).convertir_en_secondes()
        jour_de_la_semaine_reference = 2
        diff_en_seconde = secondes_date_actuelle - secondes_date_reference
        diff_en_jour = diff_en_seconde // (60 * 60 * 24)

        if abs(diff_en_jour) >= 7:
            diff_en_jour = (abs(diff_en_jour) % 7) * int(diff_en_jour/abs(diff_en_jour))

        jour_de_la_semaine = diff_en_jour + jour_de_la_semaine_reference
        if jour_de_la_semaine < 0:
            jour_de_la_semaine = 7 + jour_de_la_semaine
        if jour_de_la_semaine >= 7:
            jour_de_la_semaine = jour_de_la_semaine%7
        return jour_de_la_semaine

    def retourne_le_jour_de_la_semaine_str(self):
        return self.jours_de_la_semaine[self.retourne_le_jour_de_la_semaine()]

    def nombre_du_jour_dans_le_mois(self):
        if self.mois in self.mois_31:
            return 31
        elif self.mois in self.mois_30:
            return 30
        elif self.est_bissextile():
            return 29
        else:
            return 28

    def afficher_calendrier(self):
        semaines = self.retourne_jour_du_calendrier()
        print('----------------------------')
        print(f'{self.retourne_valeur_du_mois()} {self.annee}')
        print('----------------------------')
        print('|'.join(self.jours_de_la_semaine))
        print('----------------------------')
        for semaine in semaines:
            print('|'.join(semaine))
        print('----------------------------')


class ConversionDateTime:

    def __init__(self, annee, mois, jour, heure=0, minute=0, seconde=0, est_bissextile=False):
        self.annee, self.mois, self.jour, self.heure, self.minute, self.seconde = annee, mois, \
                                                                                  jour, heure, minute, seconde
        self.est_bissextile = est_bissextile
        if self.annee < 2000:
            raise NotImplementedError

    def convertir_en_secondes(self):
        total_seconde = 0
        total_seconde += self.retourne_annee_en_secondes()
        total_seconde += self.retourne_mois_en_secondes()
        total_seconde += self.retourne_jour_en_secondes(self.jour - 1)
        total_seconde += self.heure * 3600
        total_seconde += self.minute * 60
        total_seconde += self.seconde
        return total_seconde

    @staticmethod
    def retourne_jour_en_secondes(nombre_de_jour):
        return nombre_de_jour * 24 * 60 * 60

    def retourne_annee_en_secondes(self):
        diff = self.annee - 2000
        jours = diff * 365 + (diff % 4)
        return self.retourne_jour_en_secondes(jours)

    def retourne_mois_en_secondes(self):
        diff = self.mois - 1
        nombre_de_jour = 0
        if diff > 0:
            jour_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
            nombre_de_jour = reduce(lambda x, y: x+y, jour_par_mois[0:diff])
            if diff >= 2 and self.est_bissextile:
                nombre_de_jour += 1
        return self.retourne_jour_en_secondes(nombre_de_jour)

