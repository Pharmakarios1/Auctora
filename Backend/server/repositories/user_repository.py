from server.repositories.repository import Repository
from server.models.users import Users
from server.schemas.user_schema import GetUserSchema


class UserRepository(Repository):
    def __init__(self, db):
        super().__init__(db, Users)

    async def get_by_email(self, email: str) -> GetUserSchema:
        user = await self.get_by_attr({'email': email})
        if user:
            user = GetUserSchema.model_validate(user)
        return user if user else None
    
    async def get_by_username(self, username: str) -> GetUserSchema:
        user = await self.get_by_attr({'username': username})
        if user:
            user = GetUserSchema.model_validate(user)
        return user if user else None
