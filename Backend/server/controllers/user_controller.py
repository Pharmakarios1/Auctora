from fastapi import APIRouter


route = APIRouter(prefix='/users', tags=['users'])

@route.get('/')
def get_users():
    return {'message': 'This is a test'}