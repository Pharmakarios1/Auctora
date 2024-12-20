from server.config.app_configs import app_configs
from server.config.database import Base, engine, RedisStorage, get_db


__all__ = [
    'app_configs',
    'Base',
    'init_db',
    'sync_redis',
    'redis_store',
]


def init_db():
    """Initialize the database"""
    Base.metadata.create_all(engine)


redis_store = RedisStorage()
sync_redis = redis_store.redis