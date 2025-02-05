#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
df = pd.read_csv('/Users/santruptshekhar/Desktop/ml_rcf/modification/fire_sprinkler_data_modified.csv')
df


# In[23]:


df1 = df[['Temperature_C', 'Smoke_Density', 'Humidity_Percent', 'CO2_Level', 'Light_Intensity']]
df1.corr()


# In[24]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
import numpy as np

features = df[['Temperature_C', 'Smoke_Density', 'Humidity_Percent', 'CO2_Level', 'Light_Intensity']]
target = df['Sprinkler_Status'] 

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")

# Initialize and fit the IsolationForest model (unsupervised learning, so only X_train is used)
iso_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
iso_forest.fit(X_train)

# Predict anomalies (-1 for anomalies, 1 for normal)
train_anomaly_scores = iso_forest.predict(X_train)
test_anomaly_scores = iso_forest.predict(X_test) #prediction on test data

X_test['Sprinkler_Status'] = np.where(test_anomaly_scores == -1, 1, 0)
# The line above assigns 1 (sprinkler on) if an anomaly is detected (-1), otherwise 0 (sprinkler off)

'''Explanation of the np.where function
np.where(test_anomaly_scores == -1, 1, 0): 
Checks each element in test_anomaly_scores.
If the score is -1 (anomaly), it assigns 1 to Sprinkler_Status (sprinkler on).
Otherwise, it assigns 0 (sprinkler off).'''


print("Anomaly Detection Results on Test Set:")
print(X_test.head())


# Comparing predictions with the actual Sprinkler Status
comparison = pd.DataFrame({
    'Actual_Status': y_test.values,
    'Predicted_Status': X_test['Sprinkler_Status']
})
print("\nComparison of Actual and Predicted Sprinkler Status:")
print(comparison.head())

#calculating accuracy
accuracy = np.mean(comparison['Actual_Status'] == comparison['Predicted_Status'])
print(f"\nAccuracy of the model on test set: {accuracy * 100:.2f}%")


comparison.to_csv('/Users/santruptshekhar/Desktop/ml_rcf/modification/sprinkler_status_comparison1.csv', index=False)


# In[25]:


from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Compute the confusion matrix
conf_matrix = confusion_matrix(comparison['Actual_Status'], comparison['Predicted_Status'])
print("\nConfusion Matrix:")
print(conf_matrix)

# Calculate precision, recall, and F1 score
precision = precision_score(comparison['Actual_Status'], comparison['Predicted_Status'])
recall = recall_score(comparison['Actual_Status'], comparison['Predicted_Status'])
f1 = f1_score(comparison['Actual_Status'], comparison['Predicted_Status'])

print(f"\nPrecision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Optional: Calculate False Alarm Rate
false_alarms = conf_matrix[0, 1]  # False positives
true_negatives = conf_matrix[0, 0]
false_alarm_rate = false_alarms / (false_alarms + true_negatives)
print(f"\nFalse Alarm Rate: {false_alarm_rate * 100:.2f}%")


# In[ ]:




