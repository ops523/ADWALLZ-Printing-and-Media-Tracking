import os
import json
import qrcode
from PIL import Image

QR_FOLDER = "qr_codes"

os.makedirs(QR_FOLDER, exist_ok=True)


def create_roll_qr(
    roll_id,
    supplier,
    width_ft,
    created_date
):
    """
    Generate QR Code for a Media Roll

    Returns:
        qr_file_path
    """

    qr_data = {
        "type": "MEDIA_ROLL",
        "roll_id": roll_id,
        "supplier": supplier,
        "width_ft": width_ft,
        "created": created_date
    }

    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2
    )

    qr.add_data(json.dumps(qr_data))

    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    file_path = os.path.join(
        QR_FOLDER,
        f"{roll_id}.png"
    )

    img.save(file_path)

    return file_path


def get_qr_image(path):
    """
    Opens QR Image

    Returns PIL Image
    """

    if os.path.exists(path):
        return Image.open(path)

    return None


def qr_exists(roll_id):

    path = os.path.join(
        QR_FOLDER,
        f"{roll_id}.png"
    )

    return os.path.exists(path)


def regenerate_qr(
    roll_id,
    supplier,
    width_ft,
    created_date
):

    return create_roll_qr(
        roll_id,
        supplier,
        width_ft,
        created_date
    )
