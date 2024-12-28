import nbformat
from nbconvert import PythonExporter
from nbclient import NotebookClient
import os

def run_notebook(notebook_name, params):
    """
    Executes the given Jupyter notebook and returns the result as Python code.
    """
    # Load the notebook file
    notebook_path = os.path.join('notebooks', notebook_name)
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Set up the notebook client
    client = NotebookClient(notebook, timeout=600, resources={'parameters': params})
    
    # Execute the notebook
    client.execute()
    
    # Export the results to Python code (or any other desired format)
    exporter = PythonExporter()
    body, _ = exporter.from_notebook_node(notebook)
    return body
