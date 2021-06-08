from pymongo import MongoClient
import gridfs

def mongo_conn():
    try:
        conn=MongoClient(host="localhost")
        print("MongoDB connected", conn)
        return conn.tarea1
    except Exception as e:
        print("Error in mongo connection: ",e)
db=mongo_conn()
name="audio"
file_location="/home/fabrizio/Escritorio/"+name
file_data=open(file_location,"rb")
data=file_data.read()
fs=gridfs.GridFS(db)
fs.put(data,filename=name)
print("Upload completed")