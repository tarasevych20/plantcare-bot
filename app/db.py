from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.engine.url import make_url
from .config import get_settings

settings = get_settings()

def _normalize_db_url(url: str) -> str:
    u = make_url(url)
    q = dict(u.query) if u.query else {}
    # asyncpg не знає про sslmode / channel_binding
    q.pop("sslmode", None)
    q.pop("channel_binding", None)
    # для asyncpg достатньо ssl=true (створює дефолтний SSLContext)
    q.setdefault("ssl", "true")
    return str(u.set(query=q))

DATABASE_URL = _normalize_db_url(settings.DATABASE_URL)

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
