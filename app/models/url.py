from sqlalchemy.orm import Mapped

from app.models.base import Base


class URL(Base):
    original: Mapped[str]
    shorted: Mapped[str]
