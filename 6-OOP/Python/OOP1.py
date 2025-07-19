

# Koordinaten und Formen

# Schreiben Sie eine Klasse "Coordinate", die man unter Angabe des X- und Y-Wert erstellen kann.
# Außerdem soll die Klasse eine passende Ausgabe werfen, wenn "print(my_coordinate)" aufgerufen wird

class Coordinate:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value
    
    def __str__(self):
        return "(" +  str(self.x) + "," + str(self.y) + ")"

#c = Coordinate(2,3)
#print(c)    

# Schreiben Sie eine Methode "distance_to", welche eine weitere Koordinate übergeben bekommt und den
# Abstand zwischen den Beiden Koordinaten bestimmt. 
# Sie können dazu die "sqrt()" Funktion der "Math"-Library verwenden.

    def distance_to(self, coordinate):
        import math
        return math.sqrt((self.x - coordinate.x)**2 + (self.y - coordinate.y)**2)

c1 = Coordinate(1,1)
c2 = Coordinate(0,0)
c3 = Coordinate(1,0)

#print(c1.distance_to(c2))

# Schreiben Sie eine Klasse "Rectangle", die man unter Angabe dreier "Coordinates"-Objekte erstellen kann.
# Diese Klasse soll ebenfalls eine passende Ausgabe werfen, wenn "print(my_Rectangle)" aufgerufen wird.

class Rectangle:
    def __init__(self, first_point, second_point, third_point):
        self.first_point = first_point
        self.second_point = second_point
        self.third_point = third_point
    
    def __str__(self):
        return "Rectangle: [" + str(self.first_point) + ", " + str(self.second_point) + ", " + str(self.third_point) + "]"
    
#r = Rectangle(c1, c2, c3)
#print(r)


        
# Schreiben Sie die Methode "has_right_angle", welche mit Hilfe des Satz von Pythagoras prüft, ob 
# es sich um ein rechtwinkeliges Dreieck handelt.
# Sie können dazu die "combinations()"-Funktion aus der "itertools"-Library verwenden.

    def has_right_angle(self):
        import itertools
        distances = []
        for combination in itertools.combinations([self.first_point, self.second_point, self.third_point],2):
            distances.append(combination[0].distance_to(combination[1]))
        if distances[0] > distances[1]:
            if distances[0] > distances[2]:
                return (distances[0]**2 == distances[1]**2 + distances[2]**2)
        
       
 