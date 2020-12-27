from gestionTemps import decompositionDate


class DateFormatInvalid(Exception):
    pass


class DateTime:

    def __init__(self, date_time_string):
        self.mois_31 = [1, 3, 5, 7, 8, 10, 12]
        self.mois_30 = [4, 6, 9, 11]
        self.annee, self.mois, self.jour, self.heure, self.minute, self.seconde = decompositionDate(date_time_string)
        self.jours_de_la_semaine = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
        self.est_valide()

    def retourne_valeur_du_mois(self):
        return {
            1: 'Janvier', 2: 'Fevrier', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Decembre'
        }[self.mois]

    def est_valide(self):
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

    def est_bissextile(self):
        return self.annee % 400 == 0 or (self.annee % 4 == 0 and self.annee % 100 != 0)

    def nombre_du_jour_dans_le_mois(self):
        if self.mois in self.mois_31:
            return 31
        elif self.mois in self.mois_30:
            return 30
        elif self.est_bissextile():
            return 29
        else:
            return 28

    def retourne_jour_du_calendrier(self):
        result = []
        valeur_actuelle = -1
        premier_jour_du_mois = 3
        for i in range(5):
            semaine = []
            for j in range(7):
                if valeur_actuelle == -1 and premier_jour_du_mois == j:
                    valeur_actuelle = 0
                if 0 <= valeur_actuelle < self.nombre_du_jour_dans_le_mois():
                    valeur_actuelle += 1
                elif self.nombre_du_jour_dans_le_mois() <= valeur_actuelle:
                    valeur_actuelle = 1
                jour = '   ' if valeur_actuelle == -1 else f' {valeur_actuelle} ' if valeur_actuelle < 10 else f' {valeur_actuelle}'
                semaine.append(jour)
            result.append(semaine)
        return result

    def afficher_calendrier(self):
        print('----------------------------')
        print(self.retourne_valeur_du_mois())
        print('----------------------------')
        print('|'.join(self.jours_de_la_semaine))
        print('----------------------------')
        semaines = self.retourne_jour_du_calendrier()
        for semaine in semaines:
            print('|'.join(semaine))
        print('----------------------------')



