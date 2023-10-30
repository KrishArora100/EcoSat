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

import streamlit as st
  
st.markdown("# Welcome to EcoSat")

st.markdown("""
            To access an AI Chatbot for information about greenhouse gas (GHG) emissions and their dangers or about facility data, 
            navigate to "retreival augmented chat"\n
            To view a basic map of facilities in 2021, go to "facilities map"\n
            To view a more interactive, customizable map of facilities, go to "interactive facilities map"\n
            To view specific trends of facilities, navigate to "emissions graphs"\n
            Please note that if you are not authorized to upload data into the AI model, that feature will be disabled\n
            Also please note that there is a maximum token limit to our chatbot of 4097 tokens. If you run into an error while chatting, 
            click the rerun button found by clicking the three dots in the upper right corner. This will reset the app so you can chat again. 
            If there is still an error, try refreshing the app or trying at a later time\n
            For more information, ask the AI chatbot. Enjoy!
             """)


