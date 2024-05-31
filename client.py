import streamlit as st
import requests

st.title( ' Jokes application')
input_text = st.text_input(' Tell me joke on topic ')
def get_joke_respose(input_text):
    response = requests.post('http://localhost:8000/joke/invoke ', json={'input_text':{'topic':'input_text'}})
    return response.json()['output']
      

if st.button('Tell me joke'):
    response = get_joke_respose(input_text)
    st.write(response['joke'])