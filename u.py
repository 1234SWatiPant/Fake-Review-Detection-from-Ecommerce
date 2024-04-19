#LIBRARIES
import streamlit as st
import pickle
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import  PorterStemmer 
import re


#LOAD PICKLE FILES
model = pickle.load(open('data and pickle files/best_model.pkl','rb')) 
vectorizer = pickle.load(open('data and pickle files/count_vectorizer.pkl','rb')) 

#FOR STREAMLIT
nltk.download('stopwords')

#TEXT PREPROCESSING
sw = set(stopwords.words('english'))
def text_preprocessing(text):
    txt = TextBlob(text)
    result = txt.correct()
    removed_special_characters = re.sub("[^a-zA-Z]", " ", str(result))
    tokens = removed_special_characters.lower().split()
    stemmer = PorterStemmer()
    
    cleaned = []
    stemmed = []
    
    for token in tokens:
        if token not in sw:
            cleaned.append(token)
            
    for token in cleaned:
        token = stemmer.stem(token)
        stemmed.append(token)

    return " ".join(stemmed)

#TEXT CLASSIFICATION
def text_classification(text):
    if len(text) < 1:
        st.write("  ")
    else:
        with st.spinner("Classification in progress..."):
            cleaned_review = text_preprocessing(text)
            process = vectorizer.transform([cleaned_review]).toarray()
            prediction = model.predict(process)
            p = ''.join(str(i) for i in prediction)
        
            if p == 'True':
                st.success("The review entered is Legitimate.")
            if p == 'False':
                st.error("The review entered is Fraudulent.")

#PAGE FORMATTING AND APPLICATION
def main():
    st.title("Fraud Detection in Online Consumer Reviews Using Machine Learning Techniques")
    
    
    # --EXPANDERS--    
    abstract = st.expander("Abstract")
    if abstract:
        abstract.write("A fake review is a review written or generated without any actual experience of the product or service being reviewed (Lee et al., 2016). Because it is “written” or “generated,” a fake review can be created manually by a human writer or automatically by a computer program..")
        #st.write(abstract)
    
    links = st.expander("Related Links")
    if links:
        links.write("[Dataset utilized](https://www.kaggle.com/akudnaver/amazon-reviews-dataset)")
        
    # --CHECKBOXES--
    st.subheader("Information on the Classifier")
    if st.checkbox("About Classifer"):
        st.markdown('**Model:** Logistic Regression')
        st.markdown('**Vectorizer:** Count')
        st.markdown('**Test-Train splitting:** 40% - 60%')
        st.markdown('**Spelling Correction Library:** TextBlob')
        st.markdown('**Stemmer:** PorterStemmer')
        
    if st.checkbox("Evaluation Results"):
        st.markdown('**Accuracy:** 75%')
        st.markdown('**Precision:** 70%')
        st.markdown('**Recall:** 72%')
        st.markdown('**F-1 Score:** 75%')


    #--IMPLEMENTATION OF THE CLASSIFIER--
    st.subheader("Fake Review Classifier")
    review = st.text_area("Enter Review: ")
    if st.button("Check"):
        text_classification(review)

#RUN MAIN        
main()
