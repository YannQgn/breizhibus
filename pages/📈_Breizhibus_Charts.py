import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data.db_connection import create_connection
from assets.css.custom_css import load_css

load_css()

# Establish the database connection
connection = create_connection()

# Création du curseur
mycursor = connection.cursor()


##################################
#           Graphique 1          #
##################################


# Exécution de la requête SQL
mycursor.execute("SELECT SUM(f.nbr_passager), l.Nom as nom FROM frequentation f INNER JOIN Horaire h ON f.horaire = h.id INNER JOIN Lignes l ON h.ligne = l.id GROUP BY l.Nom ORDER BY l.Nom")
result1 = mycursor.fetchall()

df = pd.DataFrame(result1, columns=["Nbr_Passager","Nom"])

# Création d'un histogramme avec Seaborn
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(8, 5))
sns.barplot(x='Nom', y='Nbr_Passager', data=df)
plt.xlabel('Nom')
plt.ylabel('Nombre de passagers')
plt.title('Nombre de passagers par nom de ligne')

# Affichage de l'histogramme dans Streamlit
st.pyplot()


##################################
#          Graphique 2           #
##################################


# Exécution de la requête SQL
mycursor.execute('SELECT SUM(f.nbr_passager) AS nbr_passager, h.heure FROM frequentation f INNER JOIN Horaire h ON f.horaire = h.id GROUP BY f.horaire ORDER BY h.heure')
result2 = mycursor.fetchall()

df = pd.DataFrame(result2, columns=["nbr_passager","heure"])

# Création d'un graphique avec Matplotlib
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(8, 5))
plt.plot(df['heure'], df['nbr_passager'])
plt.xlabel('Heures')
plt.ylabel('Nombre de passagers')
plt.title('Nombre de passagers par heure')
plt.xticks(rotation=45)

# Affichage du graphique dans Streamlit
st.pyplot()


##################################
#          Graphique 3           #
##################################


# Exécution de la requête SQL
mycursor.execute("SELECT jour, SUM(nbr_passager) AS nbr_passager FROM frequentation GROUP BY jour ORDER BY jour ASC")
result = mycursor.fetchall()

df = pd.DataFrame(result, columns=mycursor.column_names)

# Création du camembert avec Matplotlib
plt.figure(figsize=(6,5),dpi=80)
level_counts = df['nbr_passager'].value_counts()
fig, axe = plt.subplots()
axe.pie(level_counts.index, labels=df['jour'], autopct='%1.1f%%')

# Affichage du graphique dans Streamlit
st.pyplot(fig)