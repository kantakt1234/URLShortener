from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class URL(Base):
    token: Mapped[str] = mapped_column(String(7), unique=True)
    original_url: Mapped[str] = mapped_column(unique=True)
    clicks: Mapped[int]
