import math
import os

import matplotlib.pyplot as plt
import numpy as np
import PIL.Image

# 图片路径
Image_path = 'F:\\Leung\\workspace_m\\ISAR_3d重构\\KLT_SFM_ISAR\\pic'
# 图片格式
Image_format = '.png'
# 输出路径
Out_path = Image_path + '\\out'
# 裁切边框(\pixel)
d = 0


def del_file(path):
    for dd in os.listdir(path):
        path_file = os.path.join(path, dd)  # 取文件绝对路径
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)


def getFiles(dir, suffix):  # 查找根目录，文件后缀
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename)  # =>文件名,文件后缀
            if suf == suffix:
                name_current = os.path.join(dir, filename)
                res.append(name_current)  # =>吧一串字符串组合成路径
    return res


def crop(img_ar, dd):
    arg = np.where(img_ar != [255])
    x_min = np.min(arg[0])
    x_max = np.max(arg[0])
    y_min = np.min(arg[1])
    y_max = np.max(arg[1])

    if(dd):
        x = np.shape(img_ar)
        newx1 = max(0, x_min-dd)
        newx2 = min(x[0], x_max+dd)
        newy1 = max(0, y_min-dd)
        newy2 = min(x[1], y_max+dd)
        return img_ar[newx1:newx2, newy1:newy2, :]

    crop_img = img_ar[x_min-dd:x_max+dd, y_min-dd:y_max+dd, :]
    return crop_img


if os.path.exists(Out_path):
    del_file(Out_path)
else:
    os.mkdir(Out_path)


Img_file = getFiles(Image_path, Image_format)
NUM = range(0, len(Img_file))

for i in NUM:
    img_name = str(Img_file[i])
    img = PIL.Image.open(img_name)
    img_ar = np.array(img)
    CROP_IMG = crop(img_ar, d)
    name_after = ('%s'+Image_format) % img_name.split('\\')[-1].split('.')[0]
    plt.imsave(os.path.join(Out_path, name_after), CROP_IMG)

print(f'files number: {len(Img_file)}')
print(f'Out_path: {Out_path}')
print('Done!')


# plt.figure(figsize=(16, 7))
# plt.subplot(1, 2, 1)
# plt.imshow(img)
# plt.axis('off')
# plt.subplot(1, 2, 2)
# plt.imshow(CROP_IMG)
# plt.axis('off')
# plt.show()
