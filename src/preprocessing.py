import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath="data/synthetic_maintenance.csv"):
    df = pd.read_csv(filepath)
    df = df.dropna(how='all').reset_index(drop=True)
    return df

def preprocess_features(df, target_column="maintenance_required"):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler