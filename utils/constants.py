"""
Application Constants
"""

from enum import Enum


class AssetType(str, Enum):

    MEDIA_ROLL = "MR"

    PACKAGE = "PK"

    TILE = "TL"

    PRINT_JOB = "PJ"

    DISPATCH = "DP"

    QC = "QC"

    WAREHOUSE = "WH"


class InventoryTransaction(str, Enum):

    RECEIVE = "RECEIVE"

    PRINT = "PRINT"

    DAMAGE = "DAMAGE"

    ADJUSTMENT = "ADJUSTMENT"

    TRANSFER = "TRANSFER"

    RETURN = "RETURN"

    CLOSE = "CLOSE"


class RollStatus(str, Enum):

    OPEN = "OPEN"

    IN_USE = "IN USE"

    FINISHED = "FINISHED"

    DAMAGED = "DAMAGED"

    CLOSED = "CLOSED"
