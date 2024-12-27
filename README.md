# ML-SandBox

**ML-SandBox** is an interactive web-based application designed for performing machine learning tasks on user-uploaded datasets. The platform enables users to choose specific algorithms and executes them in the backend using Jupyter Notebook, presenting the results seamlessly on the webpage.

## Key Features

- **Dataset Upload**: Users can upload their datasets directly from the webpage.
- **Algorithm Selection**: Users can choose from the following algorithms:
  - Classification
  - Find-S Algorithm
  - Candidate Key Elimination
- **Backend Processing**: The selected algorithm is executed using Jupyter Notebook in the backend.
- **Result Visualization**: The output of the algorithm is displayed in a user-friendly format on the webpage.

## Project Architecture

1. **Frontend**:
   - Provides an intuitive user interface for dataset upload and algorithm selection.
   - Built using HTML, CSS, and JavaScript for a seamless user experience.

2. **Backend**:
   - Handles the execution of machine learning algorithms using Jupyter Notebook.
   - Processes the uploaded datasets and generates the desired outputs.

3. **Integration**:
   - The frontend and backend communicate effectively to ensure smooth data transfer and result visualization.

## Getting Started

### Prerequisites

- **Python** (version >= 3.7)
- **Jupyter Notebook**
- **Node.js** (for frontend setup, if applicable)
- **Required Python Libraries**:
  - pandas
  - numpy
  - scikit-learn
  - flask (or any preferred backend framework)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ml-sandbox.git
   cd ml-sandbox
   ```

2. Set up the Python environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Start the backend server:
   ```bash
   python app.py
   ```

5. Open the frontend in your browser by navigating to the specified URL (usually `http://localhost:5000`).
