from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from app.models.url import URL
from app.urls.utils import encode_to_base62


async def get_by_token(token: str, session: AsyncSession) -> URL | None:
    stmt = select(URL).where(URL.token == token)
    result: Result = await session.execute(stmt)
    return result.scalars().one_or_none()


async def get_by_original_url(original_url: str, session: AsyncSession) -> URL | None:
    stmt = select(URL).where(URL.original_url == original_url)
    result: Result = await session.execute(stmt)
    return result.scalars().one_or_none()


async def increment_clicks(token: str, session: AsyncSession) -> URL | None:
    url = await get_by_token(token, session)
    if not url:
        return None

    url.clicks += 1

    await session.commit()
    await session.refresh(url)
    return url


async def create_url(original_url: str, session: AsyncSession) -> URL:
    url = URL(token="", original_url=original_url, clicks=0)
    session.add(url)

    await session.flush()

    token = encode_to_base62(url.id)
    url.token = token

    await session.commit()

    return url
