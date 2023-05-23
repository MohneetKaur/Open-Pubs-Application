import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
from PIL import Image
import os


df = pd.read_csv('preprocessed_df.csv')

def run():
    st.title(":green[Pub Locations 🍺🍺]")
    image = Image.open('animated_img.jpg')
    st.image(image, use_column_width=True)


    location_type = st.selectbox(
        "Select the location type:",
        ('Postal Code', 'Local Authority','Country'))

    if location_type == 'Postal Code':
        location_options = df['postcode'].unique()
        location = st.selectbox("Select the Postal Code:", location_options)
        filtered_df = df[df['postcode'] == location]
    elif location_type == 'Local Authority':
        location_options = df['local_authority'].unique()
        location = st.selectbox("Select the Local Authority:", location_options)
        filtered_df = df[df['local_authority'] == location]
    elif location_type == 'Country':
        location_options = df['country'].unique()
        location = st.selectbox("Select the Country:", location_options)
        filtered_df = df[df['country'] == location]

    if not filtered_df.empty:
        st.write("Number of Pubs in the area:", filtered_df.shape[0])

        # create a map centered at the location
        pub_map = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=12)

        # add markers for each pub location
        mc = MarkerCluster()
        for row in filtered_df.iterrows():
            mc.add_child(folium.Marker(location=[row[1]['latitude'], row[1]['longitude']], popup=row[1]['name']))
        pub_map.add_child(mc)

        # display the map
        folium_static(pub_map)
    else:
        st.write("No Pubs found in the area.")
