from datetime import time as dtime
from typing import Iterable, Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import User

DEFAULT_DAYS = [2, 5]  # вт і пт
DEFAULT_TZ = "Europe/Kyiv"
DEFAULT_TIME = dtime.fromisoformat("09:00")

async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    res = await db.execute(select(User).where(User.id == user_id))
    return res.scalar_one_or_none()

async def create_user(
    db: AsyncSession,
    *, user_id: int, username: str | None, first_name: str | None,
    tz: str = DEFAULT_TZ, notify_time: dtime = DEFAULT_TIME,
    days_selected: Iterable[int] = DEFAULT_DAYS, pre_reminder: bool = False,
) -> User:
    obj = User(
        id=user_id,
        username=username,
        first_name=first_name,
        tz=tz,
        notify_time=notify_time,
        days_selected=list(days_selected),
        pre_reminder=pre_reminder,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def ensure_user(db: AsyncSession, *, user_id: int, username: str | None, first_name: str | None):
    existing = await get_user(db, user_id)
    if existing:
        return existing, False
    created = await create_user(db, user_id=user_id, username=username, first_name=first_name)
    return created, True
