from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .config import get_settings

from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

settings = get_settings()

def _normalize_db_url(url: str) -> str:
    """
    Видаляє параметри, які ламають asyncpg (sslmode, channel_binding),
    і гарантує ssl=true. Логує лише очищений query (без паролів).
    """
    parts = urlsplit(url)
    q = dict(parse_qsl(parts.query, keep_blank_values=True))

    # прибрати все, що не підтримує asyncpg
    for k in list(q.keys()):
        if k.lower() in ("sslmode", "channel_binding"):
            q.pop(k, None)

    # гарантуємо SSL для Neon
    q.setdefault("ssl", "true")

    new_url = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(q), parts.fragment))
    print(f"[DB] normalized query -> {q}")  # безпечний лог, кредів тут немає
    return new_url

DATABASE_URL = _normalize_db_url(settings.DATABASE_URL)

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    future=True,
    # дублюємо на випадок, якщо провайдер проігнорує query
    connect_args={"ssl": True},
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
