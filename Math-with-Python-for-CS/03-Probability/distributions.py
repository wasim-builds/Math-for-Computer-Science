import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def plot_distributions():
    """
    Visualizes common probability distributions.
    """
    n_trials = 10000
    
    # 1. Normal Distribution
    mu, sigma = 0, 1
    normal_data = np.random.normal(mu, sigma, n_trials)
    
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 3, 1)
    plt.hist(normal_data, bins=50, density=True, alpha=0.7, color='blue')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title("Normal Distribution")
    
    # 2. Binomial Distribution
    n, p = 10, 0.5
    binomial_data = np.random.binomial(n, p, n_trials)
    
    plt.subplot(1, 3, 2)
    plt.hist(binomial_data, bins=11, density=True, alpha=0.7, color='green')
    plt.title(f"Binomial (n={n}, p={p})")
    
    # 3. Poisson Distribution
    lam = 3
    poisson_data = np.random.poisson(lam, n_trials)
    
    plt.subplot(1, 3, 3)
    plt.hist(poisson_data, bins=15, density=True, alpha=0.7, color='orange')
    plt.title(f"Poisson (lambda={lam})")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("--- Probability: Distributions ---")
    plot_distributions()
