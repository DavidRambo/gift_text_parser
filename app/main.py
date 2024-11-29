"""Text parser for adding multiple gift ideas in a single string."""

import fastapi
import pydantic

from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
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


class ParsedJSON(pydantic.BaseModel):
    pass
