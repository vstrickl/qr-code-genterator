import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)

qr.add_data('https://play.google.com/store/apps/details?id=net.asf.physiquemagnifique')
qr.make(fit=True)

img = qr.make_image(
    fill_color='black',
    back_color='white',
    )
img.save('googleApp.png')