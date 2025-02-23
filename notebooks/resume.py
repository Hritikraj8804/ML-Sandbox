import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load the dataset
data = pd.read_csv('../data/sample_datasets/placement_data.csv')

# Preprocess the data
X = data[['GPA', 'Internships', 'Technical_Skills', 'Communication_Skills', 'Projects']]
y = data['Placed'].apply(lambda x: 1 if x == 'Yes' else 0)

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, '../backend/model/placement_model.pkl')  