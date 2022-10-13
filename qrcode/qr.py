import pyqrcode
import png
from pyqrcode import QRCode

s = "www.thejust.vercel.app"

url = pyqrcode.create(s)

url.svg("thejust.svg" , scale = 8)

url.png('thejust.png',scale = 6)