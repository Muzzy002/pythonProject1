import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorsMessages as WRONG_EUMS
from jsonschema import validate
from src.Schemas.post import POST_SCHEMA
from src.base_classes.response import Response

def test_getting_posts():                               #pytest -s -v tests/
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)






    """assert response.status_code == 200, WRONG_EUMS.WRONG_STATUS_CODE.value
    assert len(received_posts) == 4, WRONG_EUMS.WRONG_ELEMENT_COUNT.value"""





    """{'id': 9, 'name': 'grass-spots', 'names': [
        {'language': {'name': 'de', 'url': 'https://pokeapi.co/api/v2/language/6/'},
         'name': 'Im raschelndem Gras laufen'},
        {'language': {'name': 'en', 'url': 'https://pokeapi.co/api/v2/language/9/'},
         'name': 'Walking in rustling grass'}], 'order': 2}"""
