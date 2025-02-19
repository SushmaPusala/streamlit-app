import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

#loading Model
#clf = pickle.load(open('clf.pkl','rb'))
#tfidf = pickle.load(open('tfidf.pkl','rb'))

#web app
def main():
    st.title("ATS System APi")
    st.file_uploader('Uploader Resume',type['txt','pdf'])




#python
if __name__=="__main__":
        main()

