import qrcode

data = 'https://www.youtube.com/watch?v=3aOxs3tTvP0'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/raula/OneDrive/Escritorio/Python/Sistemas de identifiación/myqr.png')