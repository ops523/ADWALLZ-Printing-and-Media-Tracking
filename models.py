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
###############################################################
# WAREHOUSE
###############################################################

class Warehouse(Base):

    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)

    warehouse_code = Column(String(30), unique=True)

    warehouse_name = Column(String(200))

    city = Column(String(100))

    state = Column(String(100))

    active = Column(Boolean, default=True)


###############################################################
# PRINTER
###############################################################

class Printer(Base):

    __tablename__ = "printers"

    id = Column(Integer, primary_key=True)

    printer_name = Column(String(200))

    city = Column(String(100))

    contact_person = Column(String(150))

    mobile = Column(String(50))

    active = Column(Boolean, default=True)


###############################################################
# MEDIA ROLL
###############################################################

class MediaRoll(Base):

    __tablename__ = "media_rolls"

    id = Column(Integer, primary_key=True)

    asset_id = Column(String(40), unique=True)

    supplier_id = Column(
        Integer,
        ForeignKey("suppliers.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("media_products.id")
    )

    warehouse_id = Column(
        Integer,
        ForeignKey("warehouses.id")
    )

    manufacturer_roll_no = Column(String(100))

    purchase_order = Column(String(100))

    invoice_number = Column(String(100))

    ordered_length_m = Column(Float)

    actual_length_m = Column(Float)

    width_ft = Column(Float)

    actual_sqft = Column(Float)

    qr_path = Column(String(300))

    status = Column(String(50))

    remarks = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    supplier = relationship("Supplier")

    product = relationship("MediaProduct")

    warehouse = relationship("Warehouse")
###############################################################
# INVENTORY LEDGER
###############################################################

class InventoryLedger(Base):

    __tablename__ = "inventory_ledger"

    id = Column(Integer, primary_key=True)

    roll_id = Column(
        Integer,
        ForeignKey("media_rolls.id")
    )

    transaction_type = Column(String(50))

    quantity_sqft = Column(Float)

    reference_type = Column(String(50))

    reference_number = Column(String(100))

    remarks = Column(Text)

    created_by = Column(String(100))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    roll = relationship("MediaRoll")
