# ConsumerBehaviorPredictor.py
# Script for predicting consumer behaviors in AI-Market-Research-and-Sustainability-Analytics

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class ConsumerBehaviorPredictor:
    def __init__(self):
        self.model = RandomForestClassifier()

    def load_data(self, filepath):
        """
        Load consumer behavior data from a file.
        """
        self.data = pd.read_csv(filepath)
        print("Data loaded successfully.")

    def preprocess_data(self):
        """
        Preprocess the data for model training.
        """
        # Assuming 'purchase_decision' is the target variable
        X = self.data.drop("purchase_decision", axis=1)
        y = self.data["purchase_decision"]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2
        )
        print("Data preprocessing completed.")

    def train_model(self):
        """
        Train the machine learning model.
        """
        self.model.fit(self.X_train, self.y_train)
        print("Model training completed.")

    def evaluate_model(self):
        """
        Evaluate the performance of the model.
        """
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        print(f"Model Accuracy: {accuracy}")


# Example usage
predictor = ConsumerBehaviorPredictor()
predictor.load_data("path/to/consumer_data.csv")
predictor.preprocess_data()
predictor.train_model()
predictor.evaluate_model()
