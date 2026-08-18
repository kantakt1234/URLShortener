from fastapi import APIRouter, status, HTTPException, Depends, Response
from fastapi.responses import RedirectResponse

from sqlalchemy.ext.asyncio import AsyncSession

from app.urls.crud import (
    get_by_token,
    create_url,
    increment_clicks,
    get_by_original_url,
    get_all,
    delete_url_by_id,
)
from app.core.db import get_session
from app.urls.schemas import URLOut

router = APIRouter()


@router.get("/")
async def get_all_urls(session: AsyncSession = Depends(get_session)) -> list[URLOut]:
    urls = await get_all(session)
    result = [URLOut.model_validate(url) for url in urls]
    return result


@router.get("/{token}")
async def redirect_to_origin(token: str, session: AsyncSession = Depends(get_session)):
    url = await get_by_token(token, session)
    if url:
        await increment_clicks(token, session)
        return RedirectResponse(
            url.original_url, status_code=status.HTTP_301_MOVED_PERMANENTLY
        )
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/")
async def create_shorted_url(
    response: Response, original_url: str, session: AsyncSession = Depends(get_session)
) -> URLOut:

    old_url = await get_by_original_url(original_url, session)
    if old_url:
        response.status_code = status.HTTP_200_OK

        result = URLOut.model_validate(old_url)
    else:
        response.status_code = status.HTTP_201_CREATED

        url = await create_url(original_url, session)
        result = URLOut.model_validate(url)

    return result


@router.delete("/{url_id}")
async def delete_url(url_id: int, session: AsyncSession = Depends(get_session)):
    result = await delete_url_by_id(url_id, session)
    if result:
        return {"result": "success"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
    )
