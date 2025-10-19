from .PatientData import PatientData
import pandas as pd

def predict_new(data :PatientData, preprocessor, model):
    
    X_new = pd.DataFrame([data.model_dump()])
    X_preprocessed  = preprocessor.transform(X_new)

    y_pred = model.predict(X_preprocessed)
    y_prob = model.predict_proba(X_preprocessed)

    prediction = ['Benign', 'Malignant']

    return {
        "Prediction" : prediction[y_pred[0]],
        'Certinity' : f"{int(y_prob[0][y_pred[0]]* 100)}%"
    }