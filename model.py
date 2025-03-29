import pandas as pd
import pickle

# failure or not
with open('model/is_failure.pkl', 'rb') as f:
    model = pickle.load(f)

def is_failure(x):
    # Select relevant columns and preprocess
    x = x[['Air temperature [K]',
           'Process temperature [K]',
           'Rotational speed [rpm]',
           'Torque [Nm]',
           'Tool wear [min]',
           'Type']]  # Include 'Type' for one-hot encoding

    # Apply one-hot encoding to the 'Type' column
    df1 = pd.get_dummies(x, columns=['Type'], drop_first=False)

    # Add missing columns if necessary (if 'Type_H', 'Type_L', 'Type_M' are not in the data)
    for col in ['Type_H', 'Type_L', 'Type_M']:
        if col not in df1.columns:
            df1[col] = 0  # Set to 0 if the column doesn't exist

    # Ensure columns are in the right order: ['Air temperature [K]', 'Process temperature [K]', ..., 'Type_H', 'Type_L', 'Type_M']
    df1 = df1[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 
               'Torque [Nm]', 'Tool wear [min]', 'Type_H', 'Type_L', 'Type_M']]

    # Make the prediction (assuming the model predicts binary outcome 0 or 1)
    prediction = model.predict(df1)
    return prediction


# failure type
with open('model/failure_type.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open('model/encoding.pkl', 'rb') as f:
    inverse = pickle.load(f)

def failure_type(x):
    x = x[['Type', 'Air temperature [K]',
       'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]',
       'Tool wear [min]']]
    df1 = pd.get_dummies(x, columns=['Type'])
    df1[['Type_H', 'Type_L', 'Type_M']] = df1[['Type_H', 'Type_L', 'Type_M']].astype(int)
    prediction = model2.predict(df1)
    return pd.Series(prediction).map(inverse)

# data transform
def data():
    df = pd.read_csv('predictive_maintenance.csv')
    return df[['Type', 'Air temperature [K]',
        'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]',
        'Tool wear [min]']]