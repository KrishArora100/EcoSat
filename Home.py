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
import plotly.express as px
import pandas as pd
  
st.markdown("# Welcome to EcoSat")

st.markdown("""
            To access EcoAI, the AI Chatbot for information about greenhouse gas (GHG) emissions and their dangers or about EPA facility data, 
            navigate to "Ask EcoAI"\n
            To view a basic map of facilities in 2021, go to "facilities map"\n
            To view a more interactive, customizable map of facilities like the one below, go to "interactive facilities map"\n
            To view specific trends of facilities, navigate to "emissions graphs"\n
            "Emissions estimations" is a work in progress. Currently it is restricted to one facility in one year\n
            Please note that if you are not authorized to upload data into EcoAI, that feature will be disabled\n
            Due to OpenAI's token limit of 8,192, EcoAI only knows around 100 of the most polluting facilities. In the future \
            with a larger token limit(like gpt 4-32k) more facilities will be added to the chatbot's information pool.
            If there are errors, try refreshing the app, clicking the \"rerun\" button, or trying at a later time\n
            For more information, ask EcoAI: "Where should I start," or "What should I ask you." Enjoy!
             """)



year = "2021"
year = st.selectbox(label="Year", options=('2011', '2012', '2013', '2014', '2015', \
                                    '2016', '2017', '2018', '2019', '2020', '2021'),
                    placeholder="2021")

num_facilities = "100"
num_facilities = st.slider(label="Number of Facilities", min_value=0, max_value=300, value=100,step=10)

df = pd.read_excel("ghgp_data_by_year.xlsx")
df.dropna(inplace=True) #in this dataset this removes all facilities that don't have data from every year(in the future make this just from 2016-2021 for Sentinel2)

#removes the text at the beginning and correctly assigns the collumns
df.columns = df.iloc[0]
df = df[1:]



df = df.sort_values(by="2021 Total reported direct emissions", ascending=False)
df = df.reset_index(drop=True)
df.to_excel("ghgp_data_by_year_formatted.xlsx")

df = df[0:int(num_facilities)]


size = df[year + ' Total reported direct emissions'].to_list()


fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name='Facility Name', 
                        zoom=3, size=size, color=size, color_continuous_scale=px.colors.diverging.RdYlGn_r,
                        custom_data=['Facility Name', year + ' Total reported direct emissions','Latitude','Longitude','Facility Id'], 
                        opacity=1, title=year + " GHG Emissions by Facility")


fig.update_traces(
    hovertemplate="<br>".join([
        "<b>Facility Name: %{customdata[0]}",
        year + " Emissions: %{customdata[1]}</b>",
        "Latitude: %{customdata[2]}",
        "Longitude: %{customdata[3]}",
        "Facility Id: %{customdata[4]}",
    ])
)




fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# create our callback function
def update_point(trace, points, selector):
    c = list(scatter.marker.color)
    s = list(scatter.marker.size)
    for i in points.point_inds:
        c[i] = '#bae2be'
        s[i] = 20
        with fig.batch_update():
            scatter.marker.color = c
            scatter.marker.size = s

scatter = fig.data[0]

scatter.on_click(update_point)

st.plotly_chart(fig)


