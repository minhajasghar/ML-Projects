#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# In[4]:


data = pd.read_csv(r"C:\Users\user\Desktop\heart.csv")


# In[5]:


data


# In[6]:


data.head()


# In[7]:


data.tail()


# In[8]:


data.describe()


# In[9]:


data.info()


# In[10]:


data.count()


# In[11]:


data.nunique()


# In[18]:


data.columns


# In[21]:


data.isnull().sum()


# In[12]:


sns.countplot(data=data, x='target', palette='viridis')
plt.title("Target Variable Distribution")
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Feature Correlation Matrix")
plt.show()


# In[13]:


numeric_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
categorical_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)
print(f"Preprocessed Training Data Shape: {X_train_preprocessed.shape}")
print(f"Preprocessed Test Data Shape: {X_test_preprocessed.shape}")


# In[14]:


models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Support Vector Machine': SVC(kernel='linear', probability=True)
}

trained_models = {}
for name, model in models.items():
    model.fit(X_train_preprocessed, y_train)
    trained_models[name] = model
    print(f"{name} trained successfully!")


# In[16]:


for name, model in trained_models.items():
    print(f"\n{name} Performance:")
    y_pred = model.predict(X_test_preprocessed)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


# In[ ]:




