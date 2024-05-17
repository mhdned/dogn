from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from databases.connection import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    # Define the relationships
    uploaded_files = relationship("File", back_populates="uploader")
    signed_files = relationship("Signature", back_populates="signer")


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uploader_id = Column(Integer, ForeignKey("user.id"))
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    extension = Column(String, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    # Define the relationships
    uploader = relationship("User", back_populates="uploaded_files")
    signatures = relationship("Signature", back_populates="file")
    documents = relationship("Document", back_populates="file")


class Signature(Base):
    __tablename__ = "signatures"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    type = Column(Enum("image", "pen", "font", name="type_signature"))
    code = Column(String)
    font = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    # Define the relationships
    file = relationship("File", back_populates="signatures")
    signer = relationship("User", back_populates="signed_files")
    documents = relationship("Document", back_populates="signature")


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_id = Column(Integer, ForeignKey("files.id"))
    signature_id = Column(Integer, ForeignKey("signatures.id"))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    # Define the relationships
    file = relationship("File", back_populates="documents")
    signature = relationship("Signature", back_populates="documents")
