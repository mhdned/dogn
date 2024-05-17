from enum import Enum
from os import makedirs, path
from typing import Annotated, Union
from uuid import uuid4

from fastapi import APIRouter, Header, HTTPException, UploadFile, status

import utils.file as FileUtils
from configs.config import config
from controllers.file import FileCRUD
from controllers.signature import SignatureCRUD
from dependencies import SessionDep
from schemas.file import NewFile
from schemas.signature import (NewSignature, NewSignatureResponse,
                               SignatureType, SingleSignature)

router = APIRouter()
    

upload_directory = f"{config["PATH"]}{config["UPLOAD_PATH"]}/signature"


@router.post(path="/add/{sign_type}",status_code=status.HTTP_201_CREATED, response_model=NewSignatureResponse)
async def upload_signature(
    db: SessionDep,
    file: UploadFile,
    sign_type: SignatureType,
    authorization: Annotated[Union[str, None], Header()] = None,
):
    ## check type of signature
    if sign_type == "pen":
        ## store file
        file_saved = await FileUtils.store_file(file,upload_directory)
        file_info = await FileUtils.metadata_file(file_saved)
        ## insert into file table
        crud_file = FileCRUD(session=db)
        crud_signature = SignatureCRUD(session=db)
        file_insert_info = NewFile(
            uploader_id=1,
            name= file_info["name"],
            path= file_info["path"],
            size= file_info["size"],
            extension= file_info["extension"],
        )
        file_inserted = crud_file.create_file(file_insert_info)
        if file_inserted:
            # return {"file" : file_inserted}
            # create instance of file for storing signature
            signature_info = NewSignature(
                file_id=file_inserted.id,
                user_id=1,
                type=sign_type,
                code=None,
                font=None
            )
            signature_inserted = crud_signature.create_signature(signature_info)
            return {"message" : "Signature is added to list", "signature" : signature_inserted}
            
        else:
            raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY,detail="Something wrong about inserting new data to database.")
    else:
        return {"message": "Currently we only support the pen tool."}

@router.get(path="/all", status_code=status.HTTP_200_OK, response_model=list[SingleSignature])
async def find_all_signature(db: SessionDep, authorization: Annotated[Union[str, None], Header()] = None):
    crud_signature = SignatureCRUD(session=db)
    all_signature = crud_signature.read_all_signature()
    if all_signature and len(all_signature) > 0:
        return all_signature
