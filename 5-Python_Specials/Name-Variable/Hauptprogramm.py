# Importieren Sie in "Hauptprogramm.py" die Beiden Funktionen aus "linear_function" und "quadratic_function".
# Ändern Sie die Beiden Dateien dabei so, dass die Test-Ausgaben nur gemacht werden, wenn die Datei selbst ausgeführt wird,
# nicht aber wenn das Hauptprogramm ausgeführt wird.
# Bestimmen Sie mit Hilfe einer Funktion "greater_until(func1, func2)" den Wert, bis zum dem die lineare Funktion größere Y-Werte produziert,
# als die Quadratische.


def greater_until(func1, func2):
    x = 0
    while(func1(x) > func2(x)):
        x += 1
    return x 

import linear_function, quadratic_function

print(greater_until(linear_function.zwei_x_plus_fünf, quadratic_function.x_squared))