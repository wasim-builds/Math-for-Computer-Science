# Math of Rummy: Combinatorics & Probability

## 1. Combinatorics of the Deal
A standard Rummy game (2 players) uses a 52-card deck. Each player gets 13 cards.

**Total unique hands:**
$$ C(52, 13) = \frac{52!}{13!(52-13)!} \approx 6.35 \times 10^{11} $$

That is over 635 billion possible starting hands! This is why **Monte Carlo Simulation** is preferred over brute-force calculation.

## 2. Probability of a "Dealt Set"
What is the probability of being dealt a "Three of a Kind" (e.g., 7♥, 7♦, 7♣)?

*   Total ways to choose 3 cards of rank '7' from 4 suits: $C(4, 3) = 4$
*   Total ways to choose 13 ranks for the set: $13$
*   Remaining 10 cards can be anything from 49 cards.

$$ P(\text{Set}) \approx \frac{13 \times 4 \times C(49, 10)}{C(52, 13)} $$

## 3. Monte Carlo Simulation
Since calculating probabilities for complex melds (Sets + Runs + Deadwood) is analytically difficult, we use **Monte Carlo**:

1.  Shuffle Deck.
2.  Deal 13 Cards.
3.  Evaluator Score (Deadwood).
4.  Repeat $N$ times.

**Law of Large Numbers**: As $N \to \infty$, the average simulation score converges to the true expected value.

## 4. Bayesian Updating (Strategy)
In Rummy, information is revealed when an opponent picks from the discard pile.

**Scenario**:
*   Opponent picks 8♠ from discard.
*   **Update**: Opponent likely has 7♠, 9♠ (Run) OR 8♥, 8♦ (Set).
*   **Strategy**: Do NOT discard 6♠, 10♠, or 8♣.

$$ P(H | E) = \frac{P(E | H) P(H)}{P(E)} $$

Where:
*   $H$: Hypothesis (Opponent has 7♠-9♠ run).
*   $E$: Evidence (Opponent picked 8♠).
