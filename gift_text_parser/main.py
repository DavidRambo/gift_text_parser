"""Text parser for adding multiple gift ideas in a single string."""

from typing import Annotated

import fastapi
import pydantic

from fastapi.middleware.cors import CORSMiddleware
from pydantic import Field

from . import utils


UrlStr = Annotated[pydantic.AnyUrl, pydantic.AfterValidator(str)]

app = fastapi.FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)


class InputText(pydantic.BaseModel):
    """Represents the data to be received from the client.

    Attributes:
        text: a string in which gift ideas are separated by a blank line
    """

    text: str


class ParsedGift(pydantic.BaseModel):
    """Represents the data to be returned to the client

    Attributes:
        parsed_text: a JSON representation of a gift idea
    """

    what: str = Field(min_length=1, max_length=255)
    link: UrlStr | None = Field(default=None)
    details: str | None = Field(default=None)


class GiftsList(pydantic.BaseModel):
    """Represents the JSON array of gift ideas parsed from the provided text.

    Attributes:
        data: a JSON array in which the objects conform to the ParsedGift model
    """

    data: list[ParsedGift]


@app.post("/parse-text", response_model=GiftsList)
def parse_text(text: InputText):
    if len(text.text) == 0:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Empty request body.",
        )

    return GiftsList(data=utils.parse_text(text.text))


@app.post("/parse-wishlist", response_model=InputText)
def parse_wishlist(wishlist: Annotated[dict[str, list], GiftsList]):
    if len(wishlist.data) == 0:
        return InputText(text="Your wish list is empty.")
    data = [dict(g) for g in wishlist.data]
    return InputText(text=utils.parse_json(data))
