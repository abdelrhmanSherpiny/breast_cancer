from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, logistic, forest
from utils.PatientData import PatientData
from utils.inference import predict_new

app = FastAPI(title=APP_NAME, version=VERSION)

@app.get('/', tags=['General'])
async def home():
    return{

        'msg' :f'Welcome to my {APP_NAME} API v{VERSION}'
    }

api_key_header = APIKeyHeader(name= "X-API-Key")
async def verify_api_key(api_key: str= Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403, detail="You are not Autharized ti use this API")
    return api_key

@app.post('/models/logistic', tags=['Logistic'])
async def logistic_predict(data: PatientData, api_key: str= Depends(verify_api_key)) -> dict:
    try:
        result = predict_new(data=data, preprocessor=preprocessor, model=logistic)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post('/models/forest', tags=['Forest'])
async def forest_predict(data: PatientData, api_key: str= Depends(verify_api_key)) -> dict:
    try:
        result = predict_new(data=data, preprocessor=preprocessor, model=forest)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

