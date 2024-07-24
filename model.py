import pandas as pd
import numpy as np
import nltk
import csv
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
pd.set_option('display.max_colwidth', None)

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def clean_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            if len(row) > 2:
                row = [row[0], ','.join(row[1:])]
            writer.writerow(row)

input_file = r'dataset.csv'
output_file = r'clean_dataset.csv'

clean_csv(input_file, output_file)

df = pd.read_csv(output_file)

stop_words = set(stopwords.words('indonesian'))

def preprocess(msg):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    msg = re.sub(r'[^\w\s]', '', msg)
    tokens = nltk.word_tokenize(msg.lower())
    tokens = [token for token in tokens if token not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]
    return ' '.join(stemmed_tokens)

def preprocess_with_stopwords(msg):
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    msg = re.sub(r'[^\w\s]', '', msg)
    tokens = nltk.word_tokenize(msg.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    stemmed_tokens = [stemmer.stem(token) for token in lemmatized_tokens]
    return ' '.join(stemmed_tokens)

class QASystem:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.questions_list = self.df['isu'].tolist()
        self.answers_list = self.df['dalil'].tolist()
        self.vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
        self.vector_isu = self.vectorizer.fit_transform([preprocess(q) for q in self.questions_list])

    def get_response(self, msg):
        processed_msg = preprocess_with_stopwords(msg)
        # print("processed_message:", processed_msg)
        
        vector_msg = self.vectorizer.transform([processed_msg])
        similarities = cosine_similarity(vector_msg, self.vector_isu)
        # print("similarities:", similarities)
        max_similarity = np.max(similarities)
        # print("max_similarity:", max_similarity)

        if max_similarity > 0:
            similar_issues = [q for q, s in zip(self.questions_list, similarities[0]) if s > 0]
            print("similar_issues:", similar_issues)
            
            answer_candidates = []
            for q in similar_issues:
                q_index = self.questions_list.index(q)
                answer_candidates.append(self.answers_list[q_index])
            # print("answer_candidates: ", answer_candidates)

            vector_similar_issues = self.vectorizer.fit_transform([preprocess_with_stopwords(q) for q in similar_issues])
            vector_msg2 = self.vectorizer.transform([processed_msg])

            final_similarities = cosine_similarity(vector_msg2, vector_similar_issues)
            closest = np.argmax(final_similarities)
            return answer_candidates[closest]
        else:
            return "Mohon maaf coba sampaikan dengan kalimat yang lain. Bukan Al-Quran yang tak tahu jawabannya, namun AI Quran merupakan sebuah model yang masih belajar untuk membantu Anda menyelesaikan masalah melalui Al-Quran, sumber pedoman yang dapat menjawab seluruh problem kehidupan. Talk like god has ready to give you the solution"

# dataframe = QASystem('clean_dataset.csv')
# dataframe.get_response('alhamdulillah saya tidak punya masalah saat ini')
