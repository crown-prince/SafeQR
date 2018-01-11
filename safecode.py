import zbar
from PIL import Image

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
img = Image.open('./PY-wensisi.jpg').convert('L')
w , h = img.size
raw = img.tostring()
zimg = zbar.Image(w, h, 'Y800', raw)

scanner.scan(zimg)

for s in zimg:
    print s.type, s.data
