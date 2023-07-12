from fastapi import FastAPI

from src.weather import router as weather_router

app = FastAPI()


@app.get('/index')
def index():
    return {"message": "hello world!"}


app.include_router(weather_router, prefix='/api')
