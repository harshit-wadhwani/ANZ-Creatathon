import nltk
nltk.download( 'punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os 
from langchain.document_loaders import PyMuPDFLoader
from langchain.vectorstores import Chroma
from langchain.llms import GooglePalm
from langchain.chains import RetrievalQA
import google.generativeai as palm

palm.configure(api_key="AIzaSyDhXDX0w_NTUiAmJKqWibB3a8PmZQynWhI")

os.environ['GOOGLE_API_KEY'] = "AIzaSyDhXDX0w_NTUiAmJKqWibB3a8PmZQynWhI"
llm = GooglePalm(temperature=0.5)

def get_proper_answer(question):
    prompt = f"{question}' Generate an answer for this usng personal pronouns"
    completion=palm.generate_text(
    model="models/text-bison-001",
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
    )
    proper_answer= completion.result.split('\n')
    return "".join(proper_answer)

def calculate_jaccard_similarity(tokens1, tokens2):
    set1 = set(tokens1)
    set2 = set(tokens2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0


def calculate_cosine_similarity(stemmed_tokens1, stemmed_tokens2):
    sentence1 = ' '.join(stemmed_tokens1)
    sentence2 = ' '.join(stemmed_tokens2)
    vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
    cosine_similarities = cosine_similarity(vectorizer[0], vectorizer[1]).flatten()
    cosine_similarity_score = cosine_similarities[0]
    return cosine_similarity_score

def get_question_answer_score(question,user_answer,proper_answer):
    score=0
    paragraph1 = proper_answer
    paragraph2 =user_answer

    # Tokenization
    tokens1 = word_tokenize(paragraph1)
    tokens2 = word_tokenize(paragraph2)

    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens1 = [word.lower() for word in tokens1 if word.isalnum() and word.lower() not in stop_words]
    filtered_tokens2 = [word.lower() for word in tokens2 if word.isalnum() and word.lower() not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens1 = [stemmer.stem(word) for word in filtered_tokens1]
    stemmed_tokens2 = [stemmer.stem(word) for word in filtered_tokens2]

    #Similarity
    jaccard_similarity = calculate_jaccard_similarity(stemmed_tokens1, stemmed_tokens2)
    print(f"Jaccard Similarity: {jaccard_similarity}")
    cosine_similarity= calculate_cosine_similarity(stemmed_tokens1, stemmed_tokens2)
    print(f"Cosine Similarity: {cosine_similarity}")

    if cosine_similarity>jaccard_similarity:
        score=int(cosine_similarity*100)
    else:
        score= int(jaccard_similarity*100)
    
    return score
    

def final_score(question, user_answer):
    ans = get_proper_answer(question)
    sc = get_question_answer_score(question, user_answer, ans)
    return sc
