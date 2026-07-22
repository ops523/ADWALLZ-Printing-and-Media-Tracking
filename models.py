from sqlalchemy import *

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from database import Base


#######################################################

class User(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True)

    username = Column(String(100),unique=True)

    password = Column(String(255))

    full_name = Column(String(200))

    role = Column(String(50))

    active = Column(Boolean,default=True)

    created_at = Column(DateTime(timezone=True),
                         server_default=func.now())

#######################################################

class Supplier(Base):

    __tablename__="suppliers"

    id=Column(Integer,primary_key=True)

    supplier_name=Column(String(200),unique=True)

    contact_person=Column(String(150))

    mobile=Column(String(50))

    email=Column(String(150))

    gst=Column(String(50))

    address=Column(Text)

    active=Column(Boolean,default=True)

#######################################################

class Manufacturer(Base):

    __tablename__="manufacturers"

    id=Column(Integer,primary_key=True)

    manufacturer_name=Column(String(200),unique=True)

    country=Column(String(100))

    active=Column(Boolean,default=True)

#######################################################

class MediaProduct(Base):

    __tablename__="media_products"

    id=Column(Integer,primary_key=True)

    manufacturer_id=Column(
        Integer,
        ForeignKey("manufacturers.id")
    )

    product_name=Column(String(200))

    gsm=Column(Float)

    width_ft=Column(Float)

    finish=Column(String(100))

    manufacturer=relationship(
        "Manufacturer"
    )
