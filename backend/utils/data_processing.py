import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def process_dataset(dataset_path):
    try:
        data = pd.read_csv(dataset_path)
        
        # Identify the last column as the target
        target_column = data.columns[-1]
        print(f"Identified target column: {target_column}")
        
        # Separate features and target
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        # Identify categorical columns
        categorical_columns = X.select_dtypes(include=['object']).columns.tolist()
        
        # Apply one-hot encoding to categorical columns
        encoder = OneHotEncoder(sparse_output=False)
        encoded_features = encoder.fit_transform(X[categorical_columns])
        
        # Create a DataFrame with the encoded features
        encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_columns))
        
        # Drop the original categorical columns and concatenate the encoded features
        X = X.drop(columns=categorical_columns)
        X = pd.concat([X, encoded_df], axis=1)
        
        return X, y, target_column
    except Exception as e:
        return f"Error processing dataset: {str(e)}"