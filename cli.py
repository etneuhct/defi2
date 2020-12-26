import argparse
import re
from gestionTemps import CalculTemps, formatDateHeure
arg_format_valeur_ajoutable = ['jour', 'heure', 'mn', 'sec']
format_attendu = 'Format attendu yyyy-mm-dd:hh:MM:ss ou yyyy-mm-dd'
message_date_invalide = f'Le format de la date est invalide\n{format_attendu}'


class DateFormatInvalid(argparse.ArgumentTypeError):
    pass


def date_validator(date_string):
    date_regex = '^[0-9]{4}-[0-9]{2}-[0-9]{2}(:[0-9]{2}:[0-9]{2}:[0-9]{2})?$'
    if not re.match(date_regex, date_string):
        raise DateFormatInvalid(message_date_invalide)
    return date_string


def set_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-date', required=False, help="Date initiale", type=date_validator)
    for item in arg_format_valeur_ajoutable:
        parser.add_argument(f'-{item}', required=False, help=f"Nombre de {item} à ajouter", type=int, default=0)
    return parser.parse_args()


def recuperer_date_initiale():
    while True:
        result = input(f'Veuillez renseigner une date. {format_attendu}:\n')
        try:
            date_validator(result)
            return result
        except DateFormatInvalid:
            print(message_date_invalide)


def recuperer_valeur_a_ajouter(format_valeur):
    while True:
        result = input(f'Veuillez renseigner un nombre de {format_valeur}:\n')
        try:
            result = int(result)
            return result
        except ValueError:
            print('Erreur. Une valeur numérique est attendue')


if __name__ == '__main__':
    args = set_arguments()
    cle_attendues = ['date', *arg_format_valeur_ajoutable]

    date, jour_a_ajouter, heure_a_ajouter, minute_a_ajouter, seconde_a_ajouter = [
        getattr(args, i) for i in cle_attendues]

    if not date:
        date = recuperer_date_initiale()

    if jour_a_ajouter == 0 and heure_a_ajouter == 0 and minute_a_ajouter == 0 and seconde_a_ajouter == 0:
        jour_a_ajouter, heure_a_ajouter, minute_a_ajouter, seconde_a_ajouter = [
            recuperer_valeur_a_ajouter(i) for i in arg_format_valeur_ajoutable
        ]

        annee, mois, jour, heure, minute, seconde = CalculTemps(date, jour_a_ajouter, heure_a_ajouter, minute_a_ajouter, seconde_a_ajouter)

        formatDateHeure(annee, mois, jour, heure, minute, seconde)

