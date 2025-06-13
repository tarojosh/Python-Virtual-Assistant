from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import sys

DATA_PATH: str = "data/data.csv"


class IntentClassifier():
    def __init__(self) -> None:
        # Load the training data for the classifier
        self.train(DATA_PATH)
    
    def train(self, filepath):
        try:
            # Obtain the data from the csv file
            data = pd.read_csv(filepath)
            X_train, y_train = data['message'], data['intent']
            
            # Create a count vectorizer to create vectors for each sentence
            self.count_vectorizer = CountVectorizer()
            X_train_counts = self.count_vectorizer.fit_transform(X_train)
            
            # Using a term frequency–inverse document frequency, we measure the importance of words to a given intent
            tf_idf = TfidfTransformer()
            X_train_tfidf = tf_idf.fit_transform(X_train_counts)
            
            self.model = MultinomialNB()
            self.model.fit(X_train_tfidf, y_train)
        
        except FileNotFoundError as e:
            print(f"[ERROR] data.csv does not exist on path '{DATA_PATH}'. Aborting...")
            sys.exit()
        
        except Exception as e:
            print(f"[ERROR] An unexpected error has occured in the training process of the Query Classifier: {e}")

    def predict(self, message: str):
        # Vectorize the message
        vectorized_message = self.count_vectorizer.transform([message])
        output: str = self.model.predict(vectorized_message)[0]  # predict() returns an array, so only select the first element
        return output


def main():
    """
    This was mainly to test if the intent classifier works as expected
    """
    query_classifier = IntentClassifier()
    messages = [
        "Heylo there",
        "Hey",
        "What day is it today?",
        "What year is it?",
        "What time is it?",
        "What is the time?",
    ]
    for msg in messages:
        print(query_classifier.predict(msg))


if __name__ == '__main__':
    main()