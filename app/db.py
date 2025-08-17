from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from .config import get_settings

settings = get_settings()
if not settings.DATABASE_URL:
    # Для локальної розробки можна тимчасово підставити SQLite, але в проді — тільки Postgres.
    # engine = create_async_engine("sqlite+aiosqlite:///./dev.db", echo=False)
    pass

engine = create_async_engine(settings.DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
