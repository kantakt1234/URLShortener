from pydantic import BaseModel, ConfigDict


class URLOut(BaseModel):
    token: str
    original_url: str

    model_config = ConfigDict(from_attributes=True)
