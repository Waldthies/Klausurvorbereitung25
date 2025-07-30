# Funktion, um die player aus einer Textdatei zu laden
def get_player(dateiname):
    player = []
    try:
        with open(dateiname, "r") as file:
            for line in file:
                # Entferne führende und nachfolgende Leerzeichen und zerlege den Eintrag am Komma
                line = line.strip()  # Entfernt Leerzeichen und Zeilenumbrüche
                daten = line.split(",")  # Teile am Komma
                if len(daten) == 2:  # Sicherstellen, dass wir genau 2 Teile (Name, Bewertung) haben
                    name = daten[0].strip()  # Vorname Nachname
                    bewertung = int(daten[1].strip())  # Bewertung als Integer
                    player.append((name, bewertung))
    except FileNotFoundError:
        print(f"Die Datei {dateiname} wurde nicht gefunden.")
    return player

# Funktion, sortieren nach OVR (insertion sort)
def sortiere_player(player):
    for i in range(1, len(player)):
        aktueller_wert = player[i] 
        j = i - 1 

        while j >= 0 and player[j][1] < aktueller_wert[1]:
            player[j + 1] = player[j]
            j -= 1 

        player[j + 1] = aktueller_wert 
    return player


# Funktion Top 5 player
def top_5_player(player):
    return player[:5]

# Funktion Differenz beseter und schlechtester Spieler
def bewertungs_differenz(player):
    max_bewertung = player[0][1]
    min_bewertung = player[-1][1]
    return max_bewertung - min_bewertung

# Funktion player Suchen
def suche_player(player, name):
    for person in player:
        if person[0].lower() == name.lower():
            return person[1] 
    return None  # Falls der player nicht gefunden wird

# Hauptlogik des Programms
def main():
    # Lade player aus der Datei
    dateiname = "playerList.txt" 
    player = get_player(dateiname)
    
    if not player:
        print("Keine playerdaten verfügbar.")
        return
    
    sortierte_player = sortiere_player(player)
    
    print("player sortiert nach Bewertung (absteigend):")
    for person in sortierte_player:
        print(f"{person[0]}: {person[1]}")
    
    top_5 = top_5_player(sortierte_player)
    print("\nTop 5 player:")
    for person in top_5:
        print(f"{person[0]}: {person[1]}")
    
    differenz = bewertungs_differenz(sortierte_player)
    print(f"\nDie Differenz zwischen der besten und schlechtesten Bewertung beträgt: {differenz}")
    
   
    name = input("\nNach welchem player möchtest du suchen? Gib den Namen ein: ")
    bewertung = suche_player(sortierte_player, name)
    
    if bewertung is not None:
        print(f"Die Bewertung von {name} ist: {bewertung}")
    else:
        print(f"player mit dem Namen '{name}' wurde nicht gefunden.")
    

main()
