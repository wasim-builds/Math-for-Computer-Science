import numpy as np
import statistics

def descriptive_statistics():
    """
    Calculates Mean, Variance, Std Dev, Median, Mode.
    """
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100]
    
    print(f"Data: {data}")
    
    # 1. Mean (Average)
    mean = np.mean(data)
    print(f"Mean: {mean:.2f}")
    
    # 2. Median (Middle Value)
    median = np.median(data)
    print(f"Median: {median:.2f}")
    
    # 3. Mode (Most Frequent)
    try:
        mode = statistics.mode(data)
        print(f"Mode: {mode}")
    except statistics.StatisticsError:
        print("Mode: No unique mode")
        
    # 4. Variance (Spread)
    variance = np.var(data, ddof=1) # ddof=1 for Sample Variance
    print(f"Variance (Sample): {variance:.2f}")
    
    # 5. Standard Deviation
    std_dev = np.std(data, ddof=1)
    print(f"Standard Deviation: {std_dev:.2f}")
    
    # 6. Percentiles
    p25 = np.percentile(data, 25)
    p75 = np.percentile(data, 75)
    print(f"25th Percentile: {p25}, 75th Percentile: {p75}")
    print(f"IQR (Interquartile Range): {p75 - p25}")

if __name__ == "__main__":
    print("--- Statistics: Descriptive ---")
    descriptive_statistics()
