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
  
st.markdown("# GHG Emissions")

st.markdown("""
             Remember to set the following in your .streamlit/secrets.toml file:
             * OPENAI_API_KEY
            * PINECONE_API_KEY, PINECONE_API_ENV, PINECONE_INDEX_NAME
            * If using EMAIL, SENDGRID_API_KEY
            * If using Dataframe, DATAFRAME_CSV as the URL for the corresponding CSV file 
            * If using the Quiz App, QUIZ_CSV as the name of the CSV file with Quiz data....
             """)


