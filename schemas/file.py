from datetime import datetime
from typing import Union

from pydantic import BaseModel


class NewFile(BaseModel):
    uploader_id: int
    name: str
    path: str
    size: int
    extension: str
