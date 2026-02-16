import numpy as np
from scipy import stats

def hypothesis_testing():
    """
    Demonstrates T-Test for hypothesis testing.
    Null Hypothesis (H0): Population mean = 50
    Alt Hypothesis (H1): Population mean != 50
    """
    # Sample data (e.g., test scores of a class)
    sample_data = [48, 52, 55, 49, 51, 53, 47, 50, 56, 54]
    
    pop_mean = 50
    
    # One-Sample T-Test
    t_stat, p_value = stats.ttest_1samp(sample_data, pop_mean)
    
    print(f"Sample Mean: {np.mean(sample_data)}")
    print(f"Hypothesized Population Mean: {pop_mean}")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    alpha = 0.05
    if p_value < alpha:
        print("Result: Reject Null Hypothesis (Significant difference)")
    else:
        print("Result: Fail to Reject Null Hypothesis (No significant difference)")

if __name__ == "__main__":
    print("--- Statistics: Hypothesis Testing ---")
    hypothesis_testing()
