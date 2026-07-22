"""
models.py
-----------------------------------------
AIMS ORM Models

Part A
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    Text
)

from sqlalchemy.sql import func

from database import Base


###########################################################
# USER
###########################################################

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    full_name = Column(
        String(200)
    )

    role = Column(
        String(50),
        default="Operator"
    )

    active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )


###########################################################
# SUPPLIER
###########################################################

class Supplier(Base):

    __tablename__ = "suppliers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    supplier_name = Column(
        String(200),
        nullable=False,
        unique=True
    )

    contact_person = Column(
        String(150)
    )

    mobile = Column(
        String(50)
    )

    email = Column(
        String(150)
    )

    gst_number = Column(
        String(50)
    )

    address = Column(
        Text
    )

    city = Column(
        String(100)
    )

    state = Column(
        String(100)
    )

    pincode = Column(
        String(20)
    )

    active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )


###########################################################
# MEDIA TYPE
###########################################################

class MediaType(Base):

    __tablename__ = "media_types"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    media_name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    width_ft = Column(
        Float,
        nullable=False
    )

    gsm = Column(
        Float
    )

    finish = Column(
        String(50)
    )

    manufacturer = Column(
        String(150)
    )

    active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
