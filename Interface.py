#############################################################
#                   FLASK ANN TEMPLATE                      #
#############################################################

import numpy as np
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib



def predict(your_parameters):
    #Replace with your saved model
    classifier=load_model('saved_model.h5')
        
    #Replace with your model scaler
    scaler = joblib.load('scaler.save')
        
    #Creating the array
    x=np.array(scaler.fit_transform([[your_parameters]]))
        
    #Predicting the output
    ypred=classifier.predict(x)
    
    #Return the value
    return ypred


