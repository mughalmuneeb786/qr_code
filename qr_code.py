import qrcode
import re 

mynamestring = 'muneeb.pro'

file_name = re.sub('[^A-Za-z0-9]+', '', mynamestring)

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

qr.add_data(mynamestring)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save(f'{file_name}.png')