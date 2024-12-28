from utils.notebook_runner import run_notebook

def run_algorithm(dataset_path, algorithm):
    """
    Run the selected algorithm notebook based on the user's input
    and return the result.
    """
    # Map algorithms to notebook filenames
    notebooks = {
        'classification': 'classification.ipynb',
        'find_s': 'find_s.ipynb',
        'candidate_key': 'candidate_key.ipynb'
    }

    # Check if the selected algorithm is valid
    if algorithm not in notebooks:
        return "Invalid algorithm selected."

    # Run the corresponding notebook
    result = run_notebook(notebooks[algorithm], {'dataset_path': dataset_path})
    
    return result
