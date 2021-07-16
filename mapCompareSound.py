import datetime

import folium
from pymongo import MongoClient
client=MongoClient("localhost")
db=client["tarea1"]
col=db["audioSubido"]

m = folium.Map(location=[-39.81422, -73.24589], zoom_start=14)
fecha=datetime.datetime(2021,4,20)
fuente="musica"
for doc in col.find():
    for doc2 in doc["archivos"]:
        la=doc2["latitud"]
        lo=doc2["longitud"]
        for doc3 in doc2["trozos"]:
            for doc4 in doc3["fuentesSonoras"]:
                if doc4["nombreFuente"]==fuente:
                    folium.Marker(location=[la, lo], popup="<i>Ubicación</i>", tooltip=doc4["nombreFuente"]).add_to(m)
m.save("index.html")