import pandas as pd

def process_dataset(dataset_path):
    try:
        data = pd.read_csv(dataset_path)
        return data
    except Exception as e:
        return f"Error processing dataset: {str(e)}"
