from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from urllib.parse import urlsplit, urlunsplit
from .config import get_settings

settings = get_settings()

class Base(DeclarativeBase):
    """Declarative Base for SQLAlchemy models."""
    pass

def _build_asyncpg_dsn(url: str) -> str:
    """
    Ігноруємо будь-який query (в т.ч. sslmode) із Neon URL,
    примусово ставимо драйвер asyncpg і ssl=true.
    """
    p = urlsplit(url)
    scheme = "postgresql+asyncpg"
    dsn = urlunsplit((scheme, p.netloc, p.path, "ssl=true", ""))
    host = p.hostname or "?"
    db = (p.path or "/").lstrip("/")
    print(f"[DB] Using asyncpg DSN host={host} db={db} ssl=true")
    return dsn

DATABASE_URL = _build_asyncpg_dsn(settings.DATABASE_URL)

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
    connect_args={"ssl": True},  # дублюємо на випадок, якщо драйвер проігнорує query
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
