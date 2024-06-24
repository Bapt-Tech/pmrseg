import datetime
import time

def temps_restant(date, heure):
    # Convertir la date et l'heure en objet datetime
    date_et_heure = datetime.datetime.strptime(date + ' ' + heure, '%d/%m/%Y %H:%M:%S')

    while datetime.datetime.now() < date_et_heure:
        temps_restant = date_et_heure - datetime.datetime.now()
        jours, secondes = temps_restant.days, temps_restant.seconds
        heures = secondes // 3600
        minutes = (secondes % 3600) // 60
        secondes = secondes % 60
        print(f"Temps restant: {jours} jours, {heures} heures, {minutes} minutes, {secondes} secondes", end="\r")
        time.sleep(1)

    print("Temps écoulé.")

# Exemple d'utilisation
date_entree = ("28/06/2024")
heure_entree = ("16:40:00")

temps_restant(date_entree, heure_entree)
