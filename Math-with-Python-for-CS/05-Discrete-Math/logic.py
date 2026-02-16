def logic_operations(p, q):
    """
    Demonstrates basic logical operations.
    """
    print(f"p = {p}, q = {q}")
    print(f"AND (p & q): {p and q}")
    print(f"OR (p | q): {p or q}")
    print(f"NOT p: {not p}")
    print(f"XOR (p ^ q): {p ^ q}")
    
    # Implication: p -> q (equivalent to not p or q)
    implication = (not p) or q
    print(f"Implication (p -> q): {implication}")
    print("-" * 20)

def print_truth_table():
    """
    Generates a truth table for (p -> q) ^ (q -> r)
    """
    print("Truth Table for (p -> q) ^ (q -> r)")
    print("p\tq\tr\tp->q\tq->r\tResult")
    
    booleans = [True, False]
    
    for p in booleans:
        for q in booleans:
            for r in booleans:
                p_imp_q = (not p) or q
                q_imp_r = (not q) or r
                result = p_imp_q and q_imp_r
                
                # Format output
                print(f"{int(p)}\t{int(q)}\t{int(r)}\t{int(p_imp_q)}\t{int(q_imp_r)}\t{int(result)}")

if __name__ == "__main__":
    print("--- Discrete Math: Logic ---")
    logic_operations(True, False)
    logic_operations(True, True)
    print_truth_table()
