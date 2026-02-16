import numpy as np
import random

def probability_simulations():
    """
    Simulates random events like Coin Toss and Dice Roll.
    """
    n_trials = 10000
    
    # 1. Coin Toss
    # 0 = Tails, 1 = Heads
    tosses = np.random.randint(0, 2, n_trials)
    heads = np.sum(tosses)
    prob_heads = heads / n_trials
    
    print(f"Coin Toss Simulation ({n_trials} trials):")
    print(f"Heads: {heads}, Probability: {prob_heads:.4f} (Expected: 0.5)")
    
    # 2. Rolling a Die
    rolls = np.random.randint(1, 7, n_trials)
    count_six = np.sum(rolls == 6)
    prob_six = count_six / n_trials
    
    print(f"\nDice Roll Simulation ({n_trials} trials):")
    print(f"Count of 6: {count_six}, Probability: {prob_six:.4f} (Expected: {1/6:.4f})")
    
    # 3. Sum of Two Dice
    dice1 = np.random.randint(1, 7, n_trials)
    dice2 = np.random.randint(1, 7, n_trials)
    sums = dice1 + dice2
    
    count_seven = np.sum(sums == 7)
    prob_seven = count_seven / n_trials
    
    print(f"\nSum of Two Dice Simulation ({n_trials} trials):")
    print(f"Sum is 7: {count_seven}, Probability: {prob_seven:.4f} (Expected: {6/36:.4f})")

if __name__ == "__main__":
    print("--- Probability: Basic Simulations ---")
    probability_simulations()
