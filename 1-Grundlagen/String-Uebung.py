# Schreiben Sie eine Funktion "string_to_array", die einen String übergeben bekommt und ein Array zurückgibt,
# das jedes Zeichen des Strings als einzelnes Element enthält.
# Für die Eingabe "Hallo Welt" soll die Funktion also "["H", "a", "l", "l", "o", " ", "W", "e", "l", "t"]" zurückgeben.

def string_to_array(my_string):
    result_list = []
    for character in my_string:
        result_list.append(character)
    return result_list

#print(string_to_array("Hallo Welt"))


# Schreiben Sie eine Funktion "division", die zwei Ganzzahlen übergeben bekommt und ein Tupel zurückgibt,
# wobei die erste Komponente des Tupel das Ergebnis der Ganzzahldivision des ersten Parameter
# durch den zweiten enthält und die zweite Komponente den Rest.
# Für division(5,2) soll die Funktion also "(2,1)" zurückgeben

def division(dividend, divisor):
    return (dividend//divisor, dividend%divisor)

#print(division(5,2))


# Schreiben Sie eine Funktion "my_division", welche die selbe Funktionalität wie "division" hat,
# jedoch keine eingebauten Divisions-Operanden wie "//" oder "%" benutzt.
# Sie können dazu Hilfsfunktionen wie "my_integer_division" oder "my_modulo" implementieren.

def my_integer_division(dividend, divisor):
    count = 0
    while(dividend - divisor > 0):
        count += 1
        dividend -= divisor
    return count
#print(my_integer_division(5,2))
    
def my_modulo(dividend, divisor):
    while(dividend - divisor > 0):
        dividend -= divisor
    return dividend
#print(my_modulo(5,2))

def my_division(dividend, divisor):
    return (my_integer_division(dividend, divisor), my_modulo(dividend, divisor))

#print(my_division(5,2))