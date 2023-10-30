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
df = df[1:]



df = df.sort_values(by="2021 Total reported direct emissions", ascending=False)
df = df.reset_index(drop=True)

facilities = df['Facility Id'].to_list()


facility = "1005310"
facility = st.text_input(label="Facility Id", value = "1005310")

if (int(facility) not in facilities):
    st.caption("facility id entered is not a valid facility id!")

else:
    df_facility = df.loc[df['Facility Id'] == int(facility)]

    emissions = []
    years = []
    for year in range(2011, 2022):
        emissions.append(df_facility.iloc[0][str(year) + ' Total reported direct emissions'])
        years.append(year)
    

    fig = px.bar(emissions, x=years, y=emissions, color=emissions, 
                 color_continuous_scale=px.colors.diverging.RdYlGn_r)
        
    st.plotly_chart(fig)
