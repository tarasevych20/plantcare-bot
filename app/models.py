from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String, Boolean, Text, Date, Time, ARRAY, ForeignKey
from .db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)  # tg_user_id
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    first_name: Mapped[str | None] = mapped_column(String, nullable=True)
    tz: Mapped[str] = mapped_column(String, default="Europe/Kyiv")
    notify_time: Mapped[str] = mapped_column(Time, nullable=False)
    days_selected: Mapped[list[int]] = mapped_column(ARRAY(Integer), nullable=False)
    pre_reminder: Mapped[bool] = mapped_column(Boolean, default=False)

class Plant(Base):
    __tablename__ = "plants"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    display_name: Mapped[str] = mapped_column(String, nullable=False)
    species_key: Mapped[str | None] = mapped_column(String, nullable=True)
    location_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)
