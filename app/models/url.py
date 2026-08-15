from sqlalchemy.orm import Mapped

from app.models.base import Base


class URL(Base):
    token: Mapped[str]
    original_url: Mapped[str]
    clicks: Mapped[int]
