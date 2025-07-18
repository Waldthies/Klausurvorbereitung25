

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
        
       
       
# Black Jack

# Schreiben Sie eine Klasse "card", die die Felder "value" und "suit" besitzt.
# Objekte der Klasse sollen außerdem in Strings umwandelbar sein. 

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
    def __str__(self):
        return str((self.suit, self.value))
    

# Schreiben Sie eine Klasse "Deck", die aus allen 52 möglichen Karten aus den Kombinationen aus den values
# "["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]"
# und den suits "["diamonds", "hearts", "spades", "clubs"]" besteht.
# Verwenden Sie eine List Comprehension.
    
    
class Deck:
    def __init__(self):
        values = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
        suits = ["diamonds", "hearts", "spades", "clubs"]
        self.cards = [Card(value, suit) for value in values for suit in suits]
        
        
# Schreiben Sie eine "__str__" für Ihr Deck, welches jede Karte des Decks ausgibt.
# Die Formatierung soll am Ende so aussehen "[("two", "heart"), ("ace", "spades")]"


    def __str__(self):
        result = "["
        for card in self.cards:
            result += str(card) + ", "
        result = result.removesuffix(", ")
        result += "]"
        return result
    

# Schreiben Sie eine Methode "shuffle", die mit Hilfe der "random"-Library und dessen "shuffle"-Methode
# die Karten des Decks durchmischt.
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
        
        
# ...

    def draw_card(self):
        return self.cards.pop()
    

class Hand:
    def __init__(self, card):
        self.cards = []
        self.ace_count = 0
        self.values = {"two" : 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}
        self.add(card)
        
    def add(self, card):
        if card.value == "ace":
            self.ace_count += 1
        self.cards.append(card)
    
    def calculate_value(self):
        result_value = 0
        for card in self.cards:
            result_value += self.values[card.value]        
        if result_value > 21 and self.ace_count > 0:
            ace_buffer = self.ace_count
            while result_value > 21 and ace_buffer > 0:
                result_value -= 10
                ace_buffer -= 1
        return result_value
                
            

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand(self.deck.draw_card())
        self.player_hand.add(self.deck.draw_card())
        self.dealer_hand = Hand(self.deck.draw_card()) 
        print("The Casinos card is: " + str(self.dealer_hand.cards[0]))
        print()
        while self.player_hand.calculate_value() <= 21:
            print("Your current hand is:")
            for card in self.player_hand.cards:
                print(card)
            print("With a total value of:", self.player_hand.calculate_value())
            user_input = input("Do you want to hit? (y/n)")   
            if user_input == "y":
                current_card = self.deck.draw_card()
                self.player_hand.add(current_card)
                print("You drew:", current_card)
            elif user_input == "n":
                print()
                while self.dealer_hand.calculate_value() < 17 and self.dealer_hand.calculate_value() < self.player_hand.calculate_value():
                    current_card = self.deck.draw_card()
                    self.dealer_hand.add(current_card)
                    print("Dealer drew:", current_card)
                
                dealer_value = self.dealer_hand.calculate_value()
                player_value = self.player_hand.calculate_value()
                print()
                print("You have a value of", player_value)
                print("The Casino has a value of", dealer_value)
                if  dealer_value >= player_value and dealer_value <= 21:
                    print("Therfore you lose. :(")
                    return
                else:
                    if dealer_value > 21:
                        print("The dealer busted! :D")
                    print("Therefore you win.")
                    print("Congratulations! :)")
                    return 
        print("You busted, therfore you lose. :(")
        

#hand = Hand(Card("ace", "hearts"))
#hand.add(Card("ace", "spades"))
#hand.add(Card("ace", "clubs"))
#print(hand.calculate_value())
game = Game()