from collections import Counter
from deck_simulation import Card

def is_set(cards):
    """
    Checks if a group of cards forms a valid set (indices 3 or 4 cards of same rank).
    Example: 7H, 7D, 7S
    """
    if len(cards) < 3 or len(cards) > 4:
        return False
    ranks = [c.rank for c in cards]
    return len(set(ranks)) == 1

def is_run(cards):
    """
    Checks if a group of cards forms a valid run (sequence of 3+ cards of same suit).
    Example: 4S, 5S, 6S
    """
    if len(cards) < 3:
        return False
    
    suits = [c.suit for c in cards]
    if len(set(suits)) != 1:
        return False
    
    # Sort by rank value
    sorted_cards = sorted(cards, key=lambda c: c.value)
    values = [c.value for c in sorted_cards]
    
    # Check for consecutive values
    for i in range(len(values) - 1):
        if values[i] + 1 != values[i+1]:
            return False
            
    return True

def evaluate_hand_score(hand):
    """
    Evaluates a Rummy hand.
    Returns a 'deadwood' score (sum of values of unmatched cards).
    Lower score is better. 0 means Gin/Rummy.
    note: This is a simplified greedy evaluator.
    """
    # 1. Sort hand
    hand.sort(key=lambda c: (c.suit, c.value))
    
    # 2. Naive check for sets and runs (In a real game, this requires backtracking to find optimal arrangement)
    # For simulation purposes, we will treat 'value' as points (Face cards=10, Ace=1 or 11, etc.)
    # Here we simplify: Number cards = value, Face = 10, Ace = 1
    
    score = 0
    for card in hand:
        if card.rank in ['J', 'Q', 'K']:
            score += 10
        elif card.rank == 'A':
            score += 1
        else:
            score += int(card.rank)
            
    # TODO: Implement full meld detection to subtract matched cards from score
    # This acts as a placeholder for the "Game Brain"
    return score

if __name__ == "__main__":
    c1 = Card('7', 'Hearts')
    c2 = Card('7', 'Diamonds')
    c3 = Card('7', 'Spades')
    print(f"Is Set {c1, c2, c3}: {is_set([c1, c2, c3])}")
    
    r1 = Card('4', 'Spades')
    r2 = Card('5', 'Spades')
    r3 = Card('6', 'Spades')
    print(f"Is Run {r1, r2, r3}: {is_run([r1, r2, r3])}")
