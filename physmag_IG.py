import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr.add_data('https://www.instagram.com/physique_magnifique/')
qr.make(fit=True)

img = qr.make_image(
    fill_color='black',
    back_color='white',
    )
img.save('physmag_IG.png')