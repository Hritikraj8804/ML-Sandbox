import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook(notebook_path, parameters):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    
    # Inject parameters into the notebook
    dataset_path = parameters['dataset_path'].replace('\\', '/')
    if 'target_column' in parameters:
        target_column = parameters['target_column']
        nb.cells.insert(0, nbformat.v4.new_code_cell(f"dataset_path = r'{dataset_path}'\ntarget_column = '{target_column}'"))
    else:
        nb.cells.insert(0, nbformat.v4.new_code_cell(f"dataset_path = r'{dataset_path}'"))
    
    try:
        ep.preprocess(nb, {'metadata': {'path': './'}})
    except Exception as e:
        return str(e)
    
    # Extract and return the output
    output = nb.cells[-1].get('outputs', [])
    if output:
        return output[0].get('text', 'No output')
    return 'No output'