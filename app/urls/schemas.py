from pydantic import BaseModel, ConfigDict, AnyUrl


class URLIn(BaseModel):
    original_url: AnyUrl

    model_config = ConfigDict(from_attributes=True)


class URLOut(URLIn):
    id: int
    token: str
    clicks: int
