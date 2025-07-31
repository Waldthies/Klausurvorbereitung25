# a)
square = [x**2 for x in range(1, 10)]

# b)
even = [x for x in range(1, 10) if x % 2 == 0]

# c)
input_reveres_words = ["Haus", "Baum", "Auto"]
reversed_words = [word[::-1] for word in input_reveres_words]

# d)
div_3_and_5 = [x for x in range(101) if x % 3 == 0 and x % 5 == 0]

# e) Erstellt eine Liste von Zahlen bis 1002, deren Anzahl der Ziffern gerade ist
original_1 = []
for i in range(1003):
    if len(str(i)) % 2 == 0:
        original_1 += [i]

alternative_1 = [i for i in range(1003) if len(str(i)) % 2 == 0]

#print(original_1 == alternative_1)

# f)
original_2 = []
i = 3
while i < 20:
    for j in range(1, 15):
        if i % j == 0:
            original_2 += [(i,j)]
    i += 2

alternative_2 = [(i, j) for i in range(3, 20, 2) for j in range(1, 15) if i % j == 0]

#print(original_2 == alternative_2)

# g)
def digit_sum(num):
    return sum(int(digit) for digit in str(num))

result = [num for num in range(1, 101) if digit_sum(num) != 0 and num % digit_sum(num) == 0]

# h) 
vowels = "aeiou"

words = []

for i in range(5):
    word = input(f"Gib {i+1}. Wort ein: ")
    words.append(word)

# Ausgabe der Liste
print("Die eingegebenen Wörter sind:", words)

result = [(word, len(word), sum(1 for char in word if char in vowels)) for word in words]
print(result)