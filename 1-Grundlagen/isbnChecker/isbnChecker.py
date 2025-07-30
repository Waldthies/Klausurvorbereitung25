def is_valid_isbn(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False
    
    total = 0
    for i in range(10):
        if isbn[i] == "X" and i == 9:
            total += (10 * (10 - i))
        elif isbn[i].isdigit():
            total += int(isbn[i]) * (10 - i)
        else:
            return False
    
    return total % 11 == 0


def validate_isbn_file(filename):
    valid_isbns = []
    invalid_isbns = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                isbn = line.strip() 
                if is_valid_isbn(isbn):
                    valid_isbns.append(isbn)
                else:
                    invalid_isbns.append(isbn)
    except FileNotFoundError:
        print(f"Die Datei {filename} wurde nicht gefunden.")
        return [], []
    
    return valid_isbns, invalid_isbns

def missing_num(isbn):
    for i in range(10):
        isbn_check = isbn.replace("x", str(i))
        if is_valid_isbn(isbn_check): 
            print(f"Valid ISBN found: {isbn_check}")
            return isbn_check
    print("No valid ISBN found.")
    return None

filename = "isbn.txt"
valid_isbns, invalid_isbns = validate_isbn_file(filename)

# Ausgabe der Ergebnisse
print("Gültige ISBN-Nummern:")
for isbn in valid_isbns:
    print(isbn)

print("\nUngültige ISBN-Nummern:")
for isbn in invalid_isbns:
    print(isbn)

print()

missing_num("3-827-41x24-0")