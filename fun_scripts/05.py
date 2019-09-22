# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os
import glob
from PIL import Image
img_path = glob.glob("F:/files/*.jpg")
path_save = "F:/files/"

for file in img_path:
    path = os.path.join(path_save, file)
    im = Image.open(file)
    im.thumbnail((1136,640))
    print(im.format, im.size, im.mode)
    im.save(path,'JPEG')
