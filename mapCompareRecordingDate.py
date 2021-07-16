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
        if doc2["fechaGrabacion"]==fecha:
            folium.Marker(location=[la, lo], popup="<i>Ubicación</i>", tooltip=doc2["fechaSubida"]).add_to(m)
m.save("index.html")