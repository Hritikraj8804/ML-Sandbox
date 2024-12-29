from flask import Flask, render_template, request, jsonify
import os
from utils.algorithms import run_algorithm

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        dataset = request.files['dataset']
        algorithm = request.form['algorithm']

        # Ensure the 'data' directory exists
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
        os.makedirs(data_dir, exist_ok=True)

        # Save dataset temporarily
        dataset_path = os.path.join(data_dir, dataset.filename)
        dataset.save(dataset_path)

        # Print statements for testing
        print(f"Received dataset: {dataset.filename}")
        print(f"Selected algorithm: {algorithm}")

        # Run the algorithm (assuming run_algorithm is defined in utils/algorithms.py)
        result = run_algorithm(dataset_path, algorithm)
        print(f"Algorithm result: {result}")

        return jsonify({"result": result, "dataset": dataset.filename, "algorithm": algorithm})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)