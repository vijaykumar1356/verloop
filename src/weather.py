from fastapi import APIRouter
from pydantic import constr
from pydantic import BaseModel
from dicttoxml import dicttoxml
import requests

from src.config import settings

router = APIRouter()


class RequestBody(BaseModel):
    city: str
    output_format: constr(pattern=r'json|xml')


@router.post('/get-current-weather')
def get_current_weather(body: RequestBody):

    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": body.city}

    headers = {
        "X-RapidAPI-Key": settings.API_KEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    output = response.json()
    formated_output = {
        "weather": f'{output["current"]["temp_c"]} C',
        "latitude": output["location"]["lat"],
        "longitude": output["location"]["lon"],
        "city": f'{output["location"]["name"]}, {output["location"]["country"]}'
    }
    if body.output_format == 'json':
        return formated_output
    elif body.output_format == 'xml':
        return dicttoxml(formated_output)

    return response.json()
