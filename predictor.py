import pickle
import pandas as pd

def predict (data, model_path): 
    '''
    data: data to get prediction on (csv) 
    model_path: path to the model (string) 
    ''' 
    model = pickle.load(open(model_path, 'rb')) 
    data = pd.read_json(data)
    selected_cols = ['Lube Oil Tank Temperature', 'Pump Journal 2 Bearing Temperature',
       'Pump Suction Strainer Differential Pressure',
       'Motor Current Phase A', 'Pump Shaft Speed',
       'Heat Recovery System Header Mass Flow', 'Motor Voltage',
       'Pump Suction Temperature', 'Pump Journal 1 Bearing Temperature',
       'Pump Thrust Bearing Temperature 1']

    data = data[selected_cols]
    prediction = model.predict(data)  
    return prediction
