import streamlit as st

st.title("Learning Machine Learning Algorithms... ")
name_of_ml_algo = st.selectbox("Choose an Algorithm", ("Linear Regression",
                                "Logistic Regression","SVR","SVC","Naive Bayes","Random Forest Tree","KNN"))
                
GOOGLE_API_KEY = "Enter_Google_api_key"

# Logic 1 --> step1: Initialize chat_model 
from langchain_google_genai import ChatGoogleGenerativeAI
chat_model = ChatGoogleGenerativeAI(google_api_key = GOOGLE_API_KEY, model = "gemini-1.5-flash")

# Logic 2 --> step2: Initialize ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system",
    "You are a friendly AI tutor with experience in DataScience and AI who tells step by step python Implemntation for a Machine learning algorithms asked by user. Explain to user by considering the user as beginer in learning machine learning. "
    ),
    ("human","Tell me a python implementation for {topic_name}.")
])

# Logic3 --> step3: Output structuring
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

# Chaining --> Binding all the three logic 1,2,3
chain = chat_prompt_template | chat_model | output_parser
user_input = { "topic_name" : name_of_ml_algo}
btn_click = st.button("see the implementation")
if btn_click == True:
    st.write(chain.invoke(user_input))


