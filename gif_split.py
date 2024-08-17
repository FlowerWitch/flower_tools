#powerby flower❀
from PIL import Image
import imageio
import os

gif_path = "./qrcode.gif"

output_path = "./gif/"

if not os.path.exists(output_path):
    os.mkdir(output_path)

gif_array = imageio.mimread(gif_path)

for i , gif_split_file in enumerate(gif_array):
    image_file = Image.fromarray(gif_split_file)

    file_name = output_path+str(i)+".png"
    image_file.save(file_name)
