from fastapi import APIRouter, Depends, BackgroundTasks
from server.config import get_db, redis_store
from server.middlewares.exception_handler import ExcRaiser
from server.schemas import (
    CreateUserSchema,
    APIResponse,
    GetUserSchema,
    LoginSchema,
    LoginToken,
    ErrorResponse,
)
from server.services import UserServices, current_user
from server.utils import Emailer
from sqlalchemy.orm import Session


route = APIRouter(prefix='/users', tags=['users'])
db = Depends(get_db)


@route.get('/')
def get_users(user: current_user) -> APIResponse[GetUserSchema]:
    """
    Get all users
    """
    return APIResponse(data=user)


@route.post(
        '/register',
        responses={
            400: {"model": ErrorResponse}
        }
    )
async def register(
    data: CreateUserSchema,
    db: Session = Depends(get_db)
) -> APIResponse:
    result = await UserServices(db).create_user(data.model_dump())

    # async with Emailer(
    #     subject="Email verification",
    #     to=result.get('email'),
    #     template_name="otp_template.html",
    #     otp=result.get('otp')
    # ) as emailer:
    #     await emailer.send_message()

    return APIResponse(
        data={
            'message':
            'User registered successfully, OTP sent to mail for verification',
        }
    )


@route.post(
        '/login',
        responses={
            401: {"model": ErrorResponse}
        }
    )
async def login(
    credentials: LoginSchema,
    db: Session = Depends(get_db)
) -> APIResponse[LoginToken]:
    token = await UserServices(db).authenticate(credentials)
    return APIResponse(data=token)
