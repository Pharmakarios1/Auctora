from fastapi import APIRouter
from server.middlewares.exception_handler import ExcRaiser


route = APIRouter(prefix='/users', tags=['users'])

@route.get('/')
def get_users(id: int = None):
    """
    Get all users
    """
    if id:
        raise ExcRaiser(status_code=404, detail='You are not meant to be here', message='User not found')
    return {'message': 'All users returned successfully'}