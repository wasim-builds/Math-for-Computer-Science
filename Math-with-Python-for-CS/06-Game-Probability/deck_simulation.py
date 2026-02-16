import random
from itertools import product

# Suits and Ranks
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {r: i for i, r in enumerate(RANKS, start=2)}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = RANK_VALUES[rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        return self.value < other.value

    def __hash__(self):
        return hash((self.rank, self.suit))

    @staticmethod
    def from_str(card_str):
        """
        Creates a Card object from a string like "7H", "10D", "AC".
        """
        card_str = card_str.strip().upper()
        if not card_str:
            raise ValueError("Empty card string")
            
        # Handle 10 (3 characters) vs others (2 characters)
        if len(card_str) == 3 and card_str.startswith('10'):
            rank = '10'
            suit_char = card_str[2]
        else:
            rank = card_str[:-1]
            suit_char = card_str[-1]
            
        suit_map = {'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs', 'S': 'Spades'}
        
        if suit_char not in suit_map:
            raise ValueError(f"Invalid suit: {suit_char}")
            
        if rank not in RANKS:
            raise ValueError(f"Invalid rank: {rank}")
            
        return Card(rank, suit_map[suit_char])

class Deck:
    def __init__(self, num_decks=1):
        self.cards = [Card(rank, suit) for rank, suit in product(RANKS, SUITS) for _ in range(num_decks)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        if n > len(self.cards):
            raise ValueError("Not enough cards in deck")
        drawn = self.cards[:n]
        self.cards = self.cards[n:]
        return drawn

    def __len__(self):
        return len(self.cards)

if __name__ == "__main__":
    deck = Deck()
    print(f"Deck created with {len(deck)} cards.")
    hand = deck.draw(13)
    print("Sample Hand:", hand)
