import streamlit as st
import os
import google.generativeai as genai


st.title("MlWhiz")



os.environ['GOOGLE_API_KEY'] = " AIzaSyAKy0DBzkk0lyMtaZym9KilBjq4SjTOg_4"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


# Creating the Model
model = genai.GenerativeModel('gemini-pro')


# Initializing chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"machine learning expert",
            "content":"Ask me Anything"
        }
    ]


# Displaying chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Processing and storing Query and Response
def process(query):
    response = model.generate_content(query)

    rel_response=response.text
    #Checking if the query is related to machine learning or not
    if model.generate_content(f"Is {rel_response} query related to machine learning or the concepts regarding it.Please only state ans in yes or no?").text=="Yes":
        # Displaying the model Message
        with st.chat_message("machine learning expert"):
            st.markdown(response.text)
    else:
        with st.chat_message("machine learning expert"):
             st.markdown("Query is not related to machine learning.")

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )


    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"machine learning expert",
            "content": response.text
        }
    )


   
# Accepting user input
query = st.chat_input("Ask me Anything")


# Calling the Function when Input is Provided
if query:
    # Displaying the Users Message
    with st.chat_message("user"):
        st.markdown(query)


    process(query)
    


