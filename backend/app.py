from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify, session
import os
import markdown
import joblib
import numpy as np
import subprocess
from utils.algorithms import run_algorithm

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.secret_key = 'supersecretkey'  # Needed for session management
visit_count = 0

data_temp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/temp'))
os.makedirs(data_temp_dir, exist_ok=True)

sample_datasets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/sample_datasets'))
os.makedirs(sample_datasets_dir, exist_ok=True)

# Path to the trained model
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/model/placement_model.pkl'))

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    return render_template('index.html', visit_count=visit_count)

@app.route('/algorithm')
def algorithm():
    return render_template('algorithm.html')

@app.route('/application')
def application():
    return render_template('application.html')

@app.route('/data')
def data():
    datasets = []
    if os.path.exists(sample_datasets_dir):
        datasets = os.listdir(sample_datasets_dir)
    return render_template('data.html', datasets=datasets)

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(sample_datasets_dir, filename, as_attachment=True)

@app.route('/docs')
def docs():
    md_file_path = os.path.join(os.path.dirname(__file__), '../docs/docs.md')
    with open(md_file_path, 'r') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)
    return render_template('docs.html', content=html_content)

@app.route('/process', methods=['POST'])
def process():
    try:
        # Run the resume.py script
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../notebooks/resume.py'))
        result = subprocess.run(['python', script_path], capture_output=True, text=True)

        # Check if the script ran successfully
        if result.returncode != 0:
            return jsonify({'error': result.stderr}), 500

        # Load the trained model
        model = joblib.load(model_path)

        # Check if the request contains form data for prediction
        if 'gpa' in request.form:
            gpa = float(request.form['gpa'])
            internships = int(request.form['internship'])
            technical_skills = len(request.form.getlist('technical[]'))
            communication = int(request.form['communication'])
            projects = int(request.form['project'])

            # Create input array for prediction
            input_data = np.array([[gpa, internships, technical_skills, communication, projects]])

            # Make prediction
            prediction = model.predict(input_data)
            result = 'Yes' if prediction[0] == 1 else 'No'

            return jsonify({'result': result})

        # Existing code for handling dataset and algorithm
        dataset = request.files['dataset']
        algorithm = request.form['algorithm']

        # Ensure the 'data' directory exists
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
        os.makedirs(data_dir, exist_ok=True)

        # Save dataset temporarily
        dataset_path = os.path.join(data_temp_dir, dataset.filename)
        dataset.save(dataset_path)

        if 'temp_files' not in session:
            session['temp_files'] = []
        session['temp_files'].append(dataset_path)

        # Print statements for testing
        print(f"Received dataset: {dataset.filename}")
        print(f"Selected algorithm: {algorithm}")

        # Run the algorithm (assuming run_algorithm is defined in utils/algorithms.py)
        result = run_algorithm(dataset_path, algorithm)
        print(f"Algorithm result: {result}")

        # Render the result.html template with the result
        return render_template('results.html', result=result, algorithm=algorithm)
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Here you can handle the form data, e.g., save it to a database or send an email
    print(f"Received contact form submission: {name}, {email}, {subject}, {message}")

    # Redirect to a thank you page or back to the contact form
    return redirect(url_for('contact_us'))

if __name__ == '__main__':
    app.run(debug=True)