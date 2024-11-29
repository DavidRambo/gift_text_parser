"""Text parser for adding multiple gift ideas in a single string."""

import fastapi
import pydantic


app = fastapi.FastAPI()


class InputText(pydantic.BaseModel):
    pass


class ParsedJSON(pydantic.BaseModel):
    pass
