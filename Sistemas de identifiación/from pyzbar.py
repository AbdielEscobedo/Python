from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/raula/OneDrive/Imágenes/Capturas de pantalla/Hola.png')

result = decode(img)

print(result)