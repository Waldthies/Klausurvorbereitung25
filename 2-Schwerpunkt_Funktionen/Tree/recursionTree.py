def baum_zeichnen(height, zeile=1):
    if zeile <= height:
        count = 2 * zeile - 1
        zeile_string = "*" * count
        print(zeile_string.center(2 * height * 2))
        baum_zeichnen(height, zeile + 1) 
    
    if zeile == height + 1:
        trunk_size = height // 2
        for i in range(trunk_size):
            print("*".center(2 * height * 2))


input_column = int(input("Wie hoch soll dein Baum sein? - "))
baum_zeichnen(input_column)
