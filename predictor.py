import pickle
import pandas as pd

def predict (data, model_path): 
    '''
    data: data to get prediction on (csv) 
    model_path: path to the model (string) 
    ''' 
    model = pickle.load(open(model_path, 'rb')) 
    data = pd.read_csv(data)

    data = data[selected_cols]
    prediction = model.predict(data)  
    return prediction
