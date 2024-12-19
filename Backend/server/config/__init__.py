from server.config.app_configs import app_configs
from server.config.database import Base, engine, RedisStorage, get_db


__all__ = [
    'app_configs',
    'Base',
    'init_db',
    'sync_redis',
    'redis_store',
]


REDIS_HOST = app_configs.DB.REDIS_HOST
REDIS_PORT = int(app_configs.DB.REDIS_PORT)
REDIS_DB = int(app_configs.DB.REDIS_DB)


def init_db():
    """Initialize the database"""
    Base.metadata.create_all(engine)

redis_store = RedisStorage(REDIS_HOST, REDIS_PORT, REDIS_DB)
sync_redis = redis_store.redis
