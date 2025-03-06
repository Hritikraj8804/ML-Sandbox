import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Here we are using the inbuilt dataset of scikit-learn
from sklearn.datasets import load_breast_cancer

# Instantiating the dataset
cancer = load_breast_cancer()
df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])
print(df.head())
print(df.shape)

# Creating the DataFrame
df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

# Importing StandardScaler module
from sklearn.preprocessing import StandardScaler

# Instantiating the Scaler
scalar = StandardScaler()

# Fitting the Scaler
scalar.fit(df)
scaled_data = scalar.transform(df)

# Importing PCA
from sklearn.decomposition import PCA

# Applying PCA (2 components)
pca = PCA(n_components=2)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

# Printing the shape of transformed data
print(x_pca.shape)

# Plotting the 2D projection of PCA data
plt.figure(figsize=(6, 4))
plt.scatter(x_pca[:, 0], x_pca[:, 1], c=cancer['target'], cmap='plasma')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')

#Creating a DataFrame to store the principal components
df_comp=pd.DataFrame(pca.components_, columns=cancer['feature_names'])

#Plotting the heatmap of PCA components
plt.figure(figsize=(14, 6))
sns.heatmap(df_comp, cmap='coolwarm') #, annot=True,fmt='.2f', linewidths=0.5)
plt.title('Heatmap of PCA Components')
plt.xlabel('Original Component')
plt.ylabel('Principal Component') 

#Displaying the plots
plt.show()
