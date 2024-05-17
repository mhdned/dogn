from os import makedirs, path
from uuid import uuid4

from fastapi import UploadFile


async def store_file(file: UploadFile, upload_path: str) -> str:
    # check file path is exists or not (true | false)
    if not path.exists(upload_path):
        makedirs(upload_path)

    # create unique name for file (str)
    unique_filename = str(uuid4()) + path.splitext(file.filename)[-1]

    # create final destination for uploaded file (str)
    final_destination = path.join(upload_path, unique_filename)

    with open(final_destination, "wb") as buffer:
        buffer.write(await file.read())

    # Return file information in the response
    return final_destination


async def metadata_file(file_path: str) -> dict:
    file_name = path.basename(file_path)
    file_size = path.getsize(file_path)
    file_format = path.splitext(file_name)[-1].lstrip(".")
    return {
        "name": file_name,
        "path": path.dirname(file_path),
        "size": file_size,
        "extension": file_format,
    }
