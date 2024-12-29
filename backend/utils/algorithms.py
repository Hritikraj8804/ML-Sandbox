from utils.notebook_runner import run_notebook
from utils.data_processing import process_dataset
import os

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

    # Debugging: Print the algorithm name
    print(f"Algorithm received: {algorithm}")

    # Check if the selected algorithm is valid
    if algorithm not in notebooks:
        return "Invalid algorithm selected."

    # Process the dataset only for classification algorithm
    if algorithm == 'classification':
        dataset_result = process_dataset(dataset_path)
        if isinstance(dataset_result, str) and dataset_result.startswith("Error"):
            return dataset_result

        X, y, target_column = dataset_result
        parameters = {'dataset_path': dataset_path, 'target_column': target_column}
    else:
        parameters = {'dataset_path': dataset_path}

    # Construct the full path to the notebook
    notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../notebooks/{notebooks[algorithm]}'))
    print(f"Notebook path: {notebook_path}")

    # Check if the notebook file exists
    if not os.path.exists(notebook_path):
        return f"Notebook file not found: {notebook_path}"

    # Run the corresponding notebook
    result = run_notebook(notebook_path, parameters)
    
    return result