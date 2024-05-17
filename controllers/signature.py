# Import ORM
from sqlalchemy.orm import Session, joinedload

# Models
from models import Signature
from schemas.signature import NewSignature, SingleSignature


# Class CRUD
class SignatureCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create_signature(self, signature_data: NewSignature) -> dict:
        new_signature = Signature(
            file_id=signature_data.file_id,
            user_id=signature_data.user_id,
            type=signature_data.type,
            code=signature_data.code,
            font=signature_data.font,
        )

        self.session.add(new_signature)
        self.session.commit()
        self.session.refresh(new_signature)

        signature_with_joined_info = (
            self.session.query(Signature)
            .options(joinedload(Signature.signer), joinedload(Signature.file))
            .filter(Signature.id == new_signature.id)
            .first()
        )

        return signature_with_joined_info

    def read_all_signature(self) -> list[SingleSignature]:
        find_all_signature = (
            self.session.query(Signature)
            .options(joinedload(Signature.signer), joinedload(Signature.file))
            .filter()
            .all()
        )
        return find_all_signature
