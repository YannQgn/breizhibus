import mysql.connector

# Configuration connexion à la bdd
def create_connection():
    config = {
    "host":"localhost",
    "port":"3307",
    "user":"admin_bzhbus",
    "password":"BS2SJy69b6tsk2",
    "database":"Breizhibusoff"
    }

    connection = mysql.connector.connect(**config)

    return connection