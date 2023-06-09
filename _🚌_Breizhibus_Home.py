import streamlit as st
import pandas as pd
from PIL import Image
from data.db_connection import create_connection
from assets.css.custom_css import load_css

load_css()

# Establish the database connection
connection = create_connection()

# Création du curseur
mycursor = connection.cursor()

st.title("Breizhibus")
# Affichage de l'image
image = Image.open('assets/pics/bzhmap.png')

st.image(image, caption='Network map Bibus 2021')

# Exécution de la requête SQL
mycursor.execute("SELECT heure,ligne,arret,l.nom, a.adresse FROM Horaire h inner join Lignes l on h.ligne = l.id inner join Arret a on h.arret = a.adresse;")
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=mycursor.column_names)
selected_line = st.selectbox('Select an adress', df['adresse'].unique())
filtered_df = df[df['adresse'] == selected_line]

# Affichage du DataFrame avec Streamlit
st.dataframe(filtered_df)