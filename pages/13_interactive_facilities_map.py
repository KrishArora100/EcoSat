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

df = pd.read_excel("ghgp_data_by_year.xlsx")
df.dropna(inplace=True) #in this dataset this removes all facilities that don't have data from every year(in the future make this just from 2016-2021 for Sentinel2)

#removes the text at the beginning and correctly assigns the collumns
df.columns = df.iloc[0]
df = df[1:200]
df = df.reset_index(drop=True)

df = df.sort_values(by="2021 Total reported direct emissions", ascending=False)

size = df['2021 Total reported direct emissions'].to_list()

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name='Facility Name', 
                        zoom=3, size=size, color=size, color_continuous_scale=px.colors.diverging.RdYlGn_r,
                        custom_data=['Facility Name', '2021 Total reported direct emissions','Latitude','Longitude'], 
                        opacity=1, title="2021 GHG Emissions by Facility")


fig.update_traces(
    hovertemplate="<br>".join([
        "<b>Facility Name: %{customdata[0]}",
        "2021 Emissions: %{customdata[1]}</b>",
        "Latitude: %{customdata[2]}",
        "Longitude: %{customdata[3]}",
    ])
)




fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)