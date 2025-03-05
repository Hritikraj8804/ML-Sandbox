import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
data = pd.read_csv('../data/sample_datasets/placement_data.csv')

# Define feature names
feature_names = ['GPA', 'Internships', 'Technical_Skills', 'Communication_Skills', 'Projects', 'Backlog']

# Preprocess the data
X = data[feature_names]
y = data['Placed'].apply(lambda x: 1 if x == 'Yes' else 0)

# Train the model with RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model with feature names
model_data = {
    'model': model,
    'feature_names': feature_names
}
joblib.dump(model_data, '../backend/model/placement_model.pkl')  