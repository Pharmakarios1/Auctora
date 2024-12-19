from passlib.context import CryptContext
from server.schemas import (
    ServiceResultModel,
    GetUserSchema
)
from server.repositories import DBAdaptor
from server.models.users import Users
from server.middlewares.exception_handler import ExcRaiser
from sqlalchemy.orm import Session


class UserServices:
    def __init__(self, db: Session):
        self.repo = DBAdaptor(db).user_repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def __check_password(self, password, hashed_password) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    async def create_user(self, data: dict) -> GetUserSchema:
        try:
            # Check if email already exist
            exist_user_email = await self.repo.get_by_email(
                data.get('email')
            )
            if exist_user_email:
                raise ExcRaiser(
                    message="Email already in use",
                    status_code=400,
                    detail="Use another email address or login with the email"
                )

            # Check if username already exist
            exist_user_username = await self.repo.get_by_username(
                data.get('username')
            )
            if exist_user_username:
                raise ExcRaiser(
                    message="Username already in use",
                    status_code=400,
                    detail="Use another username address or login with the username"
                )

            # Create new user
            else:
                new_user = await self.repo.add(data)
                if new_user:
                    result = GetUserSchema.model_validate(new_user)
                    return result

        except Exception as e:
            if type(e) == ExcRaiser:
                raise e
            raise ExcRaiser(
                message="Unable to create User",
                status_code=400,
                detail=str(e)
            )