from server.config.app_configs import app_configs
from server.config.database import Base, engine


def init_db():
    """Initialize the database"""
    Base.metadata.create_all(engine)