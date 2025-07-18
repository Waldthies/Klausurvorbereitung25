# Aufgaben zum Thema IO in Python


# Fläche von Räumen

# Schreiben Sie eine Funktion "read_rooms", welche eine Datei im "room-Format" einlesen soll.
# Das "room-Format" (Raueme.txt) besteht jeweils pro Zeile aus dem Namen des Raums, der Breite und
# und der Länge, jeweils durch einen Tabulator ("\t") getrennt.

def read_rooms(file_name):
    rooms = []
    try:
        with open(file_name, "r") as f: 
            for line in f:
                rooms.append((line.split()[0], line.split()[1:]))
        return rooms
    except:
        print("File not found or wrongly formatted.")
        return None 
rooms = read_rooms("3-Schwerpunkt_IO/Raueme.txt")
print(rooms)


# Schreiben Sie eine Funktion "calculate_square_meters", die einen Raum übergeben bekommt und das Tuple
# "Raumname, Quadratmeter" zurückgibt.

def calculate_square_meters(room):
    return (room[0], int(room[1][0])*int(room[1][1]))


# Schreiben Sie eine Funktion "sorted_square_meter_list", die mit Hilfe der zuvor definierten Funktionen 
# eine Liste mit allen "Raumname, Quadratmeter"-Tupel nach quadratmetern sortiert zurück gibt.

def sorted_sqaure_meter_list(rooms):
    unsorted_list = []
    for room in rooms:
        unsorted_list.append(calculate_square_meters(room))
    sorted_list =  sorted(unsorted_list, key= lambda x: x[1], reverse=True)
    return sorted_list

print(sorted_sqaure_meter_list(rooms))
    
