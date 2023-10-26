import folium
from streamlit_folium import st_folium, folium_static
import pandas as pd

df = pd.read_excel("ghgp_data_by_year.xlsx")
df.dropna(inplace=True) #in this dataset this removes all facilities that don't have data from every year(in the future make this just from 2016-2021 for Sentinel2)

#removes the text at the beginning and correctly assigns the collumns
df.columns = df.iloc[0]
df = df[1:100]
df = df.reset_index(drop=True)

df = df.sort_values(by="2021 Total reported direct emissions", ascending=False)

m = folium.Map(location=[df.Latitude.mean(), df.Longitude.mean()], 
                 zoom_start=3, control_scale=True)

#Loop through each row in the dataframe
for i,row in df.iterrows():
    #Setup the content of the popup
    iframe = folium.IFrame('2021 Emissions:' + str(row["2021 Total reported direct emissions"]))
    
    #Initialise the popup using the iframe
    popup = folium.Popup(iframe, min_width=300, max_width=300)
    
    #Add each row to the map
    folium.Marker(location=[row['Latitude'],row['Longitude']],
                  popup = popup, c=row['2021 Total reported direct emissions']).add_to(m)

st_data = folium_static(m, width=700)