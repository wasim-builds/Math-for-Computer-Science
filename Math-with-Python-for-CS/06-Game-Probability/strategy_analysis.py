from deck_simulation import Deck, Card
from rummy_hand_evaluator import evaluate_hand_score

def calculate_expected_value_discard(hand, possible_discards):
    """
    Calculates the Expected Value (Deadwood Score) of discarding a specific card.
    
    Logic:
    1. Remove candidate card.
    2. Simulate drawing a random card from remaining deck.
    3. Calculate new score.
    4. Average over all possible draws.
    """
    results = {}
    
    # Simulate known cards (only hand is known)
    # In a real game, you would exclude cards already seen in discard pile
    remaining_deck = Deck()
    # Remove hand cards from deck simulation
    for c in hand:
        if c in remaining_deck.cards:
            remaining_deck.cards.remove(c)
            
    for discard_card in possible_discards:
        total_score = 0
        iterations = 0
        
        # Test drawing every possible remaining card
        for draw_card in remaining_deck.cards:
            # Create temporary hand: Hand - Discard + Draw
            temp_hand = [c for c in hand if c != discard_card] + [draw_card]
            total_score += evaluate_hand_score(temp_hand)
            iterations += 1
            
        results[discard_card] = total_score / iterations
        
    return results

if __name__ == "__main__":
    deck = Deck()
    hand = deck.draw(13)
    print("Hand:", hand)
    print("Current Deadwood:", evaluate_hand_score(hand))
    
    # Evaluate discarding first 3 cards as example
    ev = calculate_expected_value_discard(hand, hand[:3])
    print("\nExpected Deadwood after discarding:")
    for card, score in ev.items():
        print(f"Discard {card}: New Expected Score = {score:.2f}")
    
    best_discard = min(ev, key=ev.get)
    print(f"\nAI Suggests Discarding: {best_discard}")
