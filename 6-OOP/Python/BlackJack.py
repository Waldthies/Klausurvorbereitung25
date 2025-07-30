import os
# Black Jack

# Schreiben Sie eine Klasse "card", die die Felder "value" und "suit" besitzt.
# Objekte der Klasse sollen außerdem in Strings umwandelbar sein. 

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
    def __str__(self):
        return str(self.value) + " of " + str(self.suit)
    

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
        
    
    def print_hand(self):    
        print("Your current hand is:")
        for card in self.cards:
            print(card)
        
    def has_blackjack(self):
        return self.calculate_value() == 21 and len(self.cards)== 2

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
    def __str__(self):
        return str(self.cards)


class Player:
    def __init__(self, money_total = 10):
        self.hand = None
        self.money_total = money_total
        self.stake = 0
        
    def raise_stake(self):
        print("Your current wealth is: ", self.money_total)
        stake = int(input("Please enter your stake for the round: "))
        while stake > self.money_total and stake > 0:
            print("You don't have enough money to bet this high.")
            stake = int(input("Please enter your stake for the current round: "))
        self.stake = stake 
        self.money_total -= stake
        
    def double_stake(self):
        self.money_total -= self.stake
        self.stake += self.stake 
        print("Doubled stake to", self.stake)
            

class Game:
    def __init__(self):
        self.player = Player()  
        while self.player.money_total > 0:
            self.play_round()      
            user_input = input("Would you like to play again? (y/n)")
            if user_input != "y":
                print("You stopped playing with a total wealth of:", self.player.money_total)
                return 
        print("You went out of money. Better luck next time!")
                

    def set_table(self):
        self.deck = Deck()
        self.deck.shuffle() 
        self.player.hand = Hand(self.deck.draw_card())
        self.dealer_hand = Hand(self.deck.draw_card())  # dealer draws 
        self.player.hand.add(self.deck.draw_card())
        self.dealer_hand.add(self.deck.draw_card())  # dealer draws again
        print("The Casinos revealed card is: " + str(self.dealer_hand.cards[0])) # reveal only one of the two cards
        print() 
    
    def play_round(self):
        os.system('cls||clear') #clears console
        self.player.raise_stake()
        self.set_table()  
        if self.player.hand.has_blackjack() and not self.dealer_hand.has_blackjack():
            print("You hit BLACKJACK. Lucky you!")
            self.player.money_total = 2.5*self.player.stake
            self.player.stake = 0
            return 
        if self.dealer_hand.cards[0].value == "ace" and self.player.money_total > self.player.stake/2:
            buys_insurance = input("Dou you want to buy an insurance against BLACKJACK?(y/n) ") == "y"
            if buys_insurance:
                self.player.money_total -= self.player.stake/2
        if self.dealer_hand.has_blackjack():
            if buys_insurance:
                print("The dealer hit BLACKJACK. Thanks to your ensurance you didn't lose any money tho.")
                self.player.money_total += self.player.stake
            else:
                print("The dealer hit BLACKJACK. You are doomed...")
            self.player.stake = 0
            return
        player_could_double_down = self.player.money_total >= (self.player.stake)
        if player_could_double_down:
            self.player.hand.print_hand()
            
            print("You have a value of", self.player.hand.calculate_value())
            wants_to_double_down = input("Do you want to double down on your bet?(y/n) ") == "y"
            if wants_to_double_down:
                self.player.double_stake()
                current_card = self.deck.draw_card()
                self.player.hand.add(current_card)
                print("You drew:", current_card)
                if self.player.hand.calculate_value() <= 21:
                    self.dealer_plays()
                else:
                    print("You busted, therefore you lose. :(")
                    self.player.stake = 0   
                return
        while self.player.hand.calculate_value() <= 21:
            if not(player_could_double_down and not wants_to_double_down):
                self.player.hand.print_hand()
                print("With a total value of:", self.player.hand.calculate_value())
            player_could_double_down = False             
            if self.player.hand.calculate_value() == 21:
                print("You hit 21! Staying.")
                self.dealer_plays()     # Finish the round by letting the dealer play
                return
            user_input = input("Do you want to hit? (y/n)")   
            if user_input == "y":
                os.system('cls||clear')
                current_card = self.deck.draw_card()
                self.player.hand.add(current_card)
                print("You drew:", current_card)
            elif user_input == "n":
                self.dealer_plays()
                return
        print("You busted, therefore you lose. :(")
        self.player.stake = 0

    def dealer_plays(self):
        print()
        print("Dealer reveals: " + str(self.dealer_hand.cards[1]))
        while self.dealer_hand.calculate_value() < 17 and self.dealer_hand.calculate_value() < self.player.hand.calculate_value():
            current_card = self.deck.draw_card()
            self.dealer_hand.add(current_card)
            print("Dealer drew:", current_card)
        
        dealer_value = self.dealer_hand.calculate_value()
        player_value = self.player.hand.calculate_value()
        print()
        print("You have a value of", player_value)
        print("The Casino has a value of", dealer_value)
        if  dealer_value > player_value and dealer_value <= 21:
            print("Therefore you lose. :(")
            self.player.stake = 0
            return
        elif  dealer_value == player_value:
            print("Push! Bets are returned")
            self.player.money_total += self.player.stake
            self.player.stake = 0
            return
        else:
            if dealer_value > 21:
                print("The dealer busted! :D")
            print("Therefore you win.")
            print("Congratulations! :)")
            self.player.money_total += 2*self.player.stake
            self.player.stake = 0
            return 
        

#hand = Hand(Card("ace", "hearts"))
#hand.add(Card("ace", "spades"))
#hand.add(Card("ace", "clubs"))
#print(hand.calculate_value())
game = Game()