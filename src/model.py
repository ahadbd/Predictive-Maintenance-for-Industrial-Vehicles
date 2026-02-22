import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from preprocessing import load_data, preprocess_features

def train_model(X, y, random_state=42):
    model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    model.fit(X, y)
    return model

if __name__ == "__main__":
    df = load_data()
    X_scaled, y, scaler = preprocess_features(df)

    model = train_model(X_scaled, y)
    y_pred = model.predict(X_scaled)

    # Add predictions to dataframe
    df['predicted_maintenance'] = y_pred
    df.to_csv("data/predictive_maintenance_results.csv", index=False)
    print("Model trained. Predictions saved to data/predictive_maintenance_results.csv")

    # Print evaluation
    print("\nClassification Report:")
    print(classification_report(y, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y, y_pred))