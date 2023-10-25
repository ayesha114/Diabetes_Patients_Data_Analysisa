import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_data(filename):
    data = pd.read_csv(filename)
    
    # Columns where zeros don't make sense and can be treated as missing values
    cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    
    for col in cols_with_zeros:
        data[col].replace(0, float('nan'), inplace=True)
        
    # Imputation
    imputer = SimpleImputer(strategy='mean')
    data[cols_with_zeros] = imputer.fit_transform(data[cols_with_zeros])
    
    # Separating the features and the labels
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    
    # Scaling the features
    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
    
    return X, y

# Split the data
X, y = preprocess_data('diabetes.csv')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
