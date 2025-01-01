import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of each column
            matrix.mean(axis=1).tolist(),  # Mean of each row
            matrix.mean().tolist()          # Mean of flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),    # Variance of each column
            matrix.var(axis=1).tolist(),    # Variance of each row
            matrix.var().tolist()            # Variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),     # Std deviation of each column
            matrix.std(axis=1).tolist(),     # Std deviation of each row
            matrix.std().tolist()             # Std deviation of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),     # Max of each column
            matrix.max(axis=1).tolist(),     # Max of each row
            matrix.max().tolist()             # Max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),     # Min of each column
            matrix.min(axis=1).tolist(),     # Min of each row
            matrix.min().tolist()             # Min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),     # Sum of each column
            matrix.sum(axis=1).tolist(),     # Sum of each row
            matrix.sum().tolist()             # Sum of flattened matrix
        ]
    }
    
    return calculations
