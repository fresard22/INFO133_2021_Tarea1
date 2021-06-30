from pymongo import MongoClient
import datetime

client=MongoClient('localhost')
db=client["tarea1"]
col=db["audioSubido"]
col.insert_one({
                "fechaSubida":datetime.datetime(2021,4,19,20,43,33),
                "fechaGrabacion":datetime.datetime(2021,4,18,14,54,2),
                "formato":"mp3",
                "duracion":43,
                "latitud":45,
                "longitud":-30,
                "ciudad":"Los Angeles",
                "naturaleza":"Interior",
                "usuario":{"nombreUsuario":"Fabrizio","apellidoUsuario":"Fresard","rut":"19810249-0"},
                "trozos":[
                       {"duracionTrozo":30,
                        "idTrozo":1,
                        "inicioTrozo":0,
                        "finTrozo":30,
                        "fuentesSonoras":[
                                       {"nombreFuente":"musica","descripcion":"Se percibe una cancion de Daft Punk de fondo","confianza":100},
                                       {"nombreFuente":"vehiculo","descripcion":"Se percibe una motocicleta acelerando","confianza":89}
                                       ]
                       },
                       {"duracionTrozo":13,
                        "idTrozo":2,
                        "inicioTrozo":30,
                        "finTrozo":43,
                        "fuentesSonoras":[
                                       {"nombreFuente":"musica","descripcion":"Se percibe una cancion de Metallica de fondo","confianza":93},
                                       {"nombreFuente":"vehiculo","descripcion":"Se percibe el claxon de un vehiculo","confianza":96}
                                       ]
                       }
                       ]
        })
print(db.list_collection_names())
print(col.count_documents({}))
for documento in col.find({}):
    print(documento)
