# consumer_feedback_analysis.py
# Script for analyzing consumer feedback and market reports in AI-Market-Research-and-Sustainability-Analytics


# For the AI-Market-Research-and-Sustainability-Analytics project, we can create a fictitious Python script focused on analyzing consumer feedback and market reports. This script, possibly named consumer_feedback_analysis.py, will be dedicated to processing, understanding, and extracting valuable insights from various forms of consumer feedback and textual market reports. This file would fit well within the consumer-insights module of the project.

# File Location:
# /AI-Market-Research-and-Sustainability-Analytics/apps/consumer-insights/consumer_feedback_analysis.py

# Content of consumer_feedback_analysis.py:

import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class ConsumerFeedbackAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.vectorizer = TfidfVectorizer(max_features=100)
    
    def load_data(self, filepath):
        """
        Load consumer feedback data from a file.
        """
        self.data = pd.read_csv(filepath)
        print("Data loaded successfully.")

    def preprocess_feedback(self):
        """
        Preprocess the feedback for analysis.
        """
        # Combining all feedback into one text for simplicity in this example
        combined_feedback = " ".join(self.data['feedback'].tolist())
        return combined_feedback

    def perform_sentiment_analysis(self, text):
        """
        Perform sentiment analysis on the provided text.
        """
        doc = self.nlp(text)
        sentiment_scores = [token.sentiment for token in doc if token.pos_ == 'ADJ']
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        return average_sentiment

    def extract_key_themes(self, text):
        """
        Extract key themes using TF-IDF and clustering.
        """
        tfidf_matrix = self.vectorizer.fit_transform([text])
        kmeans = KMeans(n_clusters=5)
        kmeans.fit(tfidf_matrix)
        feature_names = self.vectorizer.get_feature_names_out()
        top_centroids = kmeans.cluster_centers_.argsort()[:, -1:-6:-1]
        key_themes = [[feature_names[index] for index in centroid] for centroid in top_centroids]
        return key_themes

# Example usage
if __name__ == "__main__":
    analyzer = ConsumerFeedbackAnalyzer()
    analyzer.load_data('path/to/consumer_feedback.csv')
    feedback_text = analyzer.preprocess_feedback()

    sentiment = analyzer.perform_sentiment_analysis(feedback_text)
    print(f"Average Sentiment Score: {sentiment}")

    themes = analyzer.extract_key_themes(feedback_text)
    print("Key Themes from Consumer Feedback:")
    for i, theme in enumerate(themes):
        print(f"Theme {i+1}: {', '.join(theme)}")

# In this script:

# A ConsumerFeedbackAnalyzer class is created with methods to load data, preprocess consumer feedback, perform sentiment analysis, and extract key themes.
# SpaCy is used for sentiment analysis, and scikit-learn's TF-IDF vectorizer along with KMeans clustering is used to extract key themes from the feedback.
# The script assumes the presence of a CSV file containing consumer feedback.
# This script, as part of the consumer-insights module in the AI-Market-Research-and-Sustainability-Analytics project, would be crucial in understanding consumer sentiments and identifying key themes in their feedback, which is vital for market research and sustainability analysis.
