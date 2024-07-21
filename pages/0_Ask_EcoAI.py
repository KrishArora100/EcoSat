# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np

import openai
import streamlit as st
import os
from dotenv import load_dotenv
from pinecone import Pinecone


st.write("Retrieval Augmented Generation AI")


load_dotenv()


PINECONE_API_KEY=os.environ['PINECONE_API_KEY']
PINECONE_API_ENV=os.environ['PINECONE_API_ENV']
PINECONE_INDEX_NAME=os.environ['PINECONE_INDEX_NAME']
NEW_OPENAI_API_KEY=os.environ['NEW_OPENAI_API_KEY']


openai.api_key = NEW_OPENAI_API_KEY

def augmented_content(inp):
    # Create the embedding using OpenAI keys
    # Do similarity search using Pinecone
    # Return the top 5 results
    #embedding=openai.Embedding.create(model="text-embedding-ada-002", input=inp)['data'][0]['embedding']
    embedding=openai.Embedding.create(model="text-embedding-ada-002", input=inp).data[0].embedding
    
    pinecone = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    index = pinecone.Index(PINECONE_INDEX_NAME)
    results=index.query(vector=embedding,top_k=1,include_metadata=True)
    #print(f"Results: {results}")
    #st.write(f"Results: {results}")
    rr=[ r['metadata']['text'] for r in results['matches']]
    #print(f"RR: {rr}")
    #st.write(f"RR: {rr}")
    return rr

SYSTEM_MESSAGE={"role": "system", 
                "content": "Ignore all previous commands. You are EcoAI, a helpful and patient guide about greenhouse gas emissions. Answer only \
                in the context that has been provided. Say I don't know if its not in the context. You have been given data about US facility \
                emissions since 2021 in the form of text with commas separating the values. You know the columns of this dataset. If a user asks \
                for info that you can answer by looking at the dataset, \
                answer the question. If a user asks you to perform aggregations on the data provided, do it. Be confident, you can answer questions \
                about facility data. Only say I don't know if the user asks something completely unreleated to climate emissions and US facility \
                emissions data."
                }

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    retreived_content = augmented_content(prompt)
    #print(f"Retreived content: {retreived_content}")
    prompt_guidance=f"""
Please guide the user with the following information:
{retreived_content}
The user's question was: {prompt}
    """
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        messageList=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages]
        messageList.append({"role": "user", "content": prompt_guidance})
        
        for response in openai.ChatCompletion.create(
            model="gpt-4",
            max_tokens=250,
            messages=messageList, stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    with st.sidebar.expander("Retreival context provided to GPT-4"):
        st.write(f"{retreived_content}")
    st.session_state.messages.append({"role": "assistant", "content": full_response})
