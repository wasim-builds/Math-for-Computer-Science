def bayes_theorem(p_A, p_B_given_A, p_B_given_notA):
    """
    Calculates P(A|B) using Bayes' Theorem.
    
    P(A|B) = [P(B|A) * P(A)] / P(B)
    P(B) = P(B|A)*P(A) + P(B|not A)*P(not A)
    """
    p_notA = 1 - p_A
    p_B = (p_B_given_A * p_A) + (p_B_given_notA * p_notA)
    
    p_A_given_B = (p_B_given_A * p_A) / p_B
    return p_A_given_B

def run_bayes_example():
    """
    Example: Medical Diagnosis
    - P(Disease) = 0.01 (Prior)
    - P(Positive|Disease) = 0.99 (Sensitivity)
    - P(Positive|No Disease) = 0.05 (False Positive Rate)
    """
    p_disease = 0.01
    p_pos_given_disease = 0.99
    p_pos_given_no_disease = 0.05
    
    result = bayes_theorem(p_disease, p_pos_given_disease, p_pos_given_no_disease)
    
    print("--- Bayes Theorem: Medical Diagnosis ---")
    print(f"Prior Probability of Disease: {p_disease}")
    print(f"Sensitivity (True Positive Rate): {p_pos_given_disease}")
    print(f"False Positive Rate: {p_pos_given_no_disease}")
    print(f"Posterior Probability P(Disease|Positive): {result:.4f}")

if __name__ == "__main__":
    run_bayes_example()
