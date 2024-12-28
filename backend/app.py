from flask import Flask, render_template, request
from utils.algorithms import run_algorithm

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    dataset = request.files['dataset']
    algorithm = request.form['algorithm']

    # Save dataset temporarily
    dataset_path = f"data/{dataset.filename}"
    dataset.save(dataset_path)

    # Process dataset and run algorithm
    result = run_algorithm(dataset_path, algorithm)

    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
