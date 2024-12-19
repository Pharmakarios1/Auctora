from fastapi import APIRouter, Depends
from server.config import get_db
from server.middlewares.exception_handler import ExcRaiser
from server.schemas import (
    CreateUserSchema,
    APIResponse,
    GetUserSchema
)
from server.services import UserServices
from sqlalchemy.orm import Session


route = APIRouter(prefix='/users', tags=['users'])

@route.get('/')
def get_users(id: int = None):
    """
    Get all users
    """
    if id:
        raise ExcRaiser(status_code=404, detail='You are not meant to be here', message='User not found')
    return {'message': 'All users returned successfully'}


@route.post('/register')
async def register(
    data: CreateUserSchema,
    db: Session = Depends(get_db)
) -> APIResponse[GetUserSchema]:
    result = await UserServices(db).create_user(data.model_dump())
    return APIResponse(data=result)