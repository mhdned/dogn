from datetime import datetime
from enum import Enum
from typing import Union

from pydantic import BaseModel

from schemas.file import NewFile
from schemas.user import User


class SignatureType(str, Enum):
    image = "image"
    pen = "pen"
    font = "font"


class NewSignature(BaseModel):
    file_id: int
    user_id: int
    type: SignatureType
    code: Union[str, None]
    font: Union[str, None]


class SingleSignature(BaseModel):
    id: int
    file: NewFile
    signer: User
    type: SignatureType


class NewSignatureResponse(BaseModel):
    message: str
    signature: SingleSignature
