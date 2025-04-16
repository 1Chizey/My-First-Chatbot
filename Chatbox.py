import nltk
from nltk.corpus import stopwords
import streamlit as st
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")
nltk.download("omw-1.4")
# Load the text file and preprocess the data
with open("constitution_of_the_frn.txt", "r", encoding="utf-8") as f:
    data = f.read().replace('\n', ' ')
# Tokenize the text into sentences
sentences = sent_tokenize(data)

# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words("english") and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words
# Preprocess each sentence
processed_sentences = [preprocess(sentence) for sentence in sentences]

# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess(query)
    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in processed_sentences:
        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))
        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence
def chatbot(question):
    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(question)
    # Return the answer
    return most_relevant_sentence
# Streamlit app
st.set_page_config(page_title="The Constitution Of The Federal Republic Of Nigeria", page_icon="🏁")
# Title and subtitle
st.title("The Constitution Chatbot 🤖")
st.subheader("Ask me anything about the Constitution of The FRN!🏳️")

# Sidebar
st.sidebar.title("About 🎯")
st.sidebar.info(
    """
    This chatbot is designed to answer your questions about the constitution of Nigeria.
    It uses natural language processing (NLP) techniques to find the most relevant
    information from a provided text file.
    """
)
st.sidebar.title("Contact Information 📧")
st.sidebar.info("Email ✉️: chizeyfrancis@gmail.com")
st.sidebar.info("Phone 📞: +234 8135874318")
st.sidebar.title("Help 🆘")
st.sidebar.info("For any assistance, kindly refer to the documentation or contact support.")

st.sidebar.title("Credits")
st.sidebar.info(
    """
    Created by [Chizey](https://github.com/1Chizey).

    Powered by [Streamlit](https://streamlit.io) and [NLTK](https://www.nltk.org).
    """
)
#footer
st.info("© 2025 Chizey/Nigeria. All rights reserved.")

# Main content
query = st.text_input("Enter a question:")

if query:
    answer = chatbot(query)
    st.write("**Answer:**", answer)
else:
    st.write("Please enter a question.")