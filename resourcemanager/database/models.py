"""Module responsible for defining all relational database models."""
from sqlalchemy import Column, Integer, String, Float

from resourcemanager.database import Base


class User(Base):
    """Defines model for the User."""
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(80), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)

    # TODO: add role
    # TODO: hash password

    def __init__(self, username: str, email: str, password_hash: str) -> None:
        """Initialize User."""
        self.username = username
        self.email = email
        self.password = password_hash


class Product(Base):
    """Defines model for the Product."""
    __tablename__ = 'products'
    id = Column(Integer, autoincrement=True, primary_key=True)
    manufacturer_name = Column(String(80), unique=False, nullable=False)
    model_name = Column(String(80), unique=False, nullable=False)
    price = Column(Float(30), unique=False, nullable=False)
    quantity = Column(Integer, unique=False, nullable=False)

    def __init__(self, manufacturer_name: str, model_name: str, price: float, quantity: int) -> None:
        """Initialize User."""
        self.manufacturer_name = manufacturer_name
        self.model_name = model_name
        self.price = price
        self.quantity = quantity