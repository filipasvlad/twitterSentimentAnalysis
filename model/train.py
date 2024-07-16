import time
import numpy as np
import pandas as pd
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from nltk.corpus import stopwords
import re
from gensim.models import Word2Vec
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns


def process_data():
    column_name = ['target', 'id', 'data', 'flag', 'user', 'text']
    twitter_data = pd.read_csv('model\\data\\training.1600000.processed.noemoticon.csv', names=column_name, encoding="ISO-8859-1")
    twitter_data.replace({'target': {4: 1}}, inplace=True)

    port_stem = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    def preprocess(text):
        # Removing URLS
        text = re.sub(r"https?://\S+|www\.\S+", " ", text)

        # Removing html tags
        text = re.sub(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", " ", text)

        # Removing the Punctuation
        text = re.sub(r"[^\w\s]", " ", text)

        # Removing words that have numbers
        text = re.sub(r"\w*\d\w*", " ", text)

        # Removing Digits
        text = re.sub(r"[0-9]+", " ", text)

        # Cleaning white spaces
        text = re.sub(r"\s+", " ", text).strip()

        text = text.lower()
        # Check stop words
        tokens = []
        for token in text.split():
            if token not in stop_words and len(token) > 2:
                tokens.append(port_stem.stem(token))
        return " ".join(tokens)

    twitter_data['stemmed_content'] = twitter_data['text'].apply(preprocess)

    twitter_data.to_csv('model\\data\\processed_tweets.csv', index=False)

def save_vectorizer(vectorizer):
    with open('model\\artifacts\\vectorizer.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)

def save_model(model):
    pickle.dump(model, open("model\\artifacts\\model.sav", 'wb'))

def vectorize_with_tfidf(X_train, X_test):
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    return vectorizer, X_train, X_test

def vectorize_with_count(X_train, X_test):
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    return vectorizer, X_train, X_test

def vectorize_with_word2vec(X_train, X_test, twitter_data):
    class MyCorpus:
        def __iter__(self):
            for sentence in twitter_data['stemmed_content'].values:
                yield sentence.split()

    sentences = MyCorpus()
    trained_w2v = Word2Vec(sentences=sentences, min_count=10, vector_size=100)

    def w2v_of_sentences(sentences, wv):
        vectors = np.zeros((len(sentences), wv.vector_size))
        for i, sentence in enumerate(sentences):
            sum_vector = np.zeros((1, wv.vector_size))
            tokens = sentence.split()
            for token in tokens:
                try:
                    sum_vector += wv[token]
                except:
                    pass
            if len(tokens) > 0:
                vectors[i] = sum_vector / len(tokens)
            else:
                vectors[i] = sum_vector
        return vectors

    X_train = w2v_of_sentences(X_train, trained_w2v.wv)
    X_test = w2v_of_sentences(X_test, trained_w2v.wv)
    return X_train, X_test


def train_random_forest(X_train, Y_train):
    np.random.seed(0)
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=50,
        min_samples_split=30,
        n_jobs=-1,
        random_state=42
    )
    model.fit(X_train, Y_train)
    return model

def train_logistic_regression(X_train, Y_train):
    model = LogisticRegression(solver='liblinear')
    model.fit(X_train, Y_train)
    return model

def plot_confusion_matrix(conf_matrix):
    plt.figure(figsize=(3.7, 3.7))
    ax = sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False, annot_kws={"size": 16})
    ax.set_xlabel('Reale', labelpad=2)
    ax.set_ylabel('Prezise', labelpad=2)
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    plt.xticks(ticks=[0.5, 1.5], labels=['Pozitive', 'Negative'], rotation=0)
    ax.set_yticklabels(['Pozitive', 'Negative'], rotation=90, ha='right')
    plt.show()

def evaluate_model(model, X_test, Y_test):
    X_test_prediction = model.predict(X_test)
    conf_matrix = confusion_matrix(Y_test, X_test_prediction)
    TN, FP, FN, TP = conf_matrix.ravel()
    print(f"Accuracy: {(TP + TN) / (TP + TN + FN + FP)}")
    print(f"Precision: {TP / (TP + FP)}")
    print(f"Recall: {TP / (TP + FN)}")
    print(f"F1 Score: {TP / (TP + (FN + FP) / 2)}")
    #plot_confusion_matrix([[TP, FP], [FN, TN]])

def classify_sentiments_with_logistic_regression_count():
    twitter_data = pd.read_csv('model\\data\\processed_tweets.csv', encoding="ISO-8859-1")
    twitter_data = twitter_data.dropna(subset=['stemmed_content'])
    X = twitter_data['stemmed_content'].values
    Y = twitter_data['target'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, stratify=Y, random_state=42)

    start_time = time.time()

    vectorizer, X_train, X_test = vectorize_with_count(X_train, X_test)
    model = train_logistic_regression(X_train, Y_train)
    evaluate_model(model, X_test, Y_test)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")

    save_vectorizer(vectorizer)
    save_model(model)

def classify_sentiments_with_logistic_regression_tfidf():
    twitter_data = pd.read_csv('model\\data\\processed_tweets.csv', encoding="ISO-8859-1")
    twitter_data = twitter_data.dropna(subset=['stemmed_content'])
    X = twitter_data['stemmed_content'].values
    Y = twitter_data['target'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, stratify=Y, random_state=42)
    start_time = time.time()

    vectorizer, X_train, X_test = vectorize_with_tfidf(X_train, X_test)
    model = train_logistic_regression(X_train, Y_train)
    evaluate_model(model, X_test, Y_test)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")

    save_vectorizer(vectorizer)
    save_model(model)


def classify_sentiments_with_logistic_regression_word2vec():
    twitter_data = pd.read_csv('model\\data\\processed_tweets.csv', encoding="ISO-8859-1")
    twitter_data = twitter_data.dropna(subset=['stemmed_content'])
    X = twitter_data['stemmed_content'].values
    Y = twitter_data['target'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, stratify=Y, random_state=42)

    start_time = time.time()

    X_train, X_test = vectorize_with_word2vec(X_train, X_test, twitter_data)
    model = train_logistic_regression(X_train, Y_train)
    evaluate_model(model, X_test, Y_test)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")


def classify_sentiments_with_random_forest_count():
    twitter_data = pd.read_csv('model\\data\\processed_tweets.csv', encoding="ISO-8859-1")
    twitter_data = twitter_data.dropna(subset=['stemmed_content'])
    X = twitter_data['stemmed_content'].values
    Y = twitter_data['target'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, stratify=Y, random_state=42)

    start_time = time.time()

    vectorizer, X_train, X_test = vectorize_with_count(X_train, X_test)
    model = train_random_forest(X_train, Y_train)
    evaluate_model(model, X_test, Y_test)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")

    save_vectorizer(vectorizer)
    save_model(model)

def classify_sentiments_with_random_forest_tfidf():
    twitter_data = pd.read_csv('model\\data\\processed_tweets.csv', encoding="ISO-8859-1")
    twitter_data = twitter_data.dropna(subset=['stemmed_content'])
    X = twitter_data['stemmed_content'].values
    Y = twitter_data['target'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, stratify=Y, random_state=42)

    start_time = time.time()

    vectorizer, X_train, X_test = vectorize_with_tfidf(X_train, X_test)
    model = train_random_forest(X_train, Y_train)
    evaluate_model(model, X_test, Y_test)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")

    save_vectorizer(vectorizer)
    save_model(model)


def classify_sentiments_with_random_forest_word2vec():
    twitter_data = pd.read_csv('model\\data\\processed_tweets.csv', encoding="ISO-8859-1")
    twitter_data = twitter_data.dropna(subset=['stemmed_content'])
    X = twitter_data['stemmed_content'].values
    Y = twitter_data['target'].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, stratify=Y, random_state=42)

    start_time = time.time()

    X_train, X_test = vectorize_with_word2vec(X_train, X_test, twitter_data)
    model = train_random_forest(X_train, Y_train)
    evaluate_model(model, X_test, Y_test)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Timpul de execuție: {execution_time} secunde")


def run():
    while True:
        print("1. LogisticRegression + CountVectorizer\n2. LogisticRegression + TfidfVectorizer\n3. LogisticRegression + Word2Vec")
        print("4. RandomForest + CountVectorizer\n5. RandomForest + TfidfVectorizer\n6. RandomForest + Word2Vec")
        nr = int(input(">>> "))
        match nr:
            case 1:
                classify_sentiments_with_logistic_regression_count()
            case 2:
                classify_sentiments_with_logistic_regression_tfidf()
            case 3:
                classify_sentiments_with_logistic_regression_word2vec()
            case 4:
                classify_sentiments_with_random_forest_count()
            case 5:
                classify_sentiments_with_random_forest_tfidf()
            case 6:
                classify_sentiments_with_random_forest_word2vec()
            case _:
                print("Valoare invalidă")