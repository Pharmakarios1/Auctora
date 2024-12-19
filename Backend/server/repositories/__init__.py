from server.repositories.repository import Repository
from server.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session


class DBAdaptor:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)