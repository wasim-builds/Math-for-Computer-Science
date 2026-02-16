import random
from deck_simulation import Deck
from rummy_hand_evaluator import evaluate_hand_score

def monte_carlo_simulation(num_simulations=1000):
    """
    Simulates Rummy hands to estimate the distribution of "deadwood" scores.
    This helps answer: "What is a good starting hand?"
    """
    scores = []
    
    for _ in range(num_simulations):
        deck = Deck()
        # Deal 13 cards
        hand = deck.draw(13)
        score = evaluate_hand_score(hand)
        scores.append(score)
        
    avg_score = sum(scores) / len(scores)
    min_score = min(scores)
    max_score = max(scores)
    
    return {
        "simulations": num_simulations,
        "average_score": avg_score,
        "min_score": min_score,
        "max_score": max_score,
        "scores": scores # Return raw data for histogram
    }

if __name__ == "__main__":
    print("Running Monte Carlo Simulation for Rummy Hands...")
    results = monte_carlo_simulation(5000)
    print(f"Simulations: {results['simulations']}")
    print(f"Average Hand Score (Deadwood): {results['average_score']:.2f}")
    print(f"Best Hand Found: {results['min_score']}")
    print(f"Worst Hand Found: {results['max_score']}")
