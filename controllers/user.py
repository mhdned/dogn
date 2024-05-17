# Import ORM
from sqlalchemy.orm import Session

# Models
from models import User


# Class CRUD
class UserCRUD:
    def __init__(self, session: Session):
        self.session = session

    def read_all_user(self):
        return self.session.query(User).filter().all()
