## Working ##
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGSMITH_PROJECT"] = "Simple Q&A ChatBot with OpenAI"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A ChatBot with Ollama"

#Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helful assistant. Please response to the user queries"),
        ("user", "Question:{question}")
    ]
)

def generate_response(question, engine, temperature):
    llm=Ollama(model=engine)
    outpur_parser=StrOutputParser()
    chain=prompt|llm|outpur_parser
    answer=chain.invoke({'question':question})
    return answer

st.title("Simple Q&A chatbot ")

## Drop down to select various LLM Models
engine = st.sidebar.selectbox("Select a Model", ["phi3"])

## Slider from temperature
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main Interface for user Input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, engine, temperature)
    st.write(response)
else:
    st.write("Please provide the query")
