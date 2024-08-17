#powerby flower❀
import os
from pyzbar.pyzbar import decode
from PIL import Image

qr_dir = "./gif"

for i in range(38):
    filename = str(i)+".png"
    filepath = os.path.join(qr_dir,filename)
    image_file = Image.open(filepath)
    qr_info = decode(image_file)
    print(qr_info[0].data.decode("utf-8"),end="")
