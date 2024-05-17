# Import ORM
from sqlalchemy.orm import Session

# Models
from models import File
from schemas.file import NewFile


# Class CRUD
class FileCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_file(self, file_data: NewFile):
        new_file = File(
            uploader_id=file_data.uploader_id,
            name=file_data.name,
            path=file_data.path,
            size=file_data.size,
            extension=file_data.extension,
        )
        self.session.add(new_file)
        self.session.commit()
        self.session.refresh(new_file)
        return new_file

    def read_all_file(self):
        return self.session.query(File).filter().all()
