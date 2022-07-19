# importing the required libraries
import pymongo
import pprint
import json
import warnings
import pandas as pd, numpy as np
warnings.filterwarnings('ignore')

# connect to the mongoclient
client = pymongo.MongoClient('mongodb://localhost:27017')

# get the database
database = client['intern']

sensor_data = database.get_collection("sensor_data")
column_names = sensor_data.distinct("sensor_name")

df1 = pd.DataFrame(sensor_data.find_one({"sensor_name":'Motor Voltage'}, 
                                    {"data":1})["data"], 
                                    columns=["timestamp",'value']).rename(columns ={"value":'Motor Voltage'})[['timestamp']]

for col in column_names:
    df2 = pd.DataFrame(sensor_data.find_one({"sensor_name":col}, 
                                    {"data":1})["data"], 
                                    columns=["timestamp",'value']).rename(columns ={"value":col})
                                    
    df1 =df1.merge(df2, on='timestamp')   

df1.to_csv("data/sample_sensor_data.csv")