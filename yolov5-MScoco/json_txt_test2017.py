import os
from shutil import copyfile

src_path = 'F:/datasets/coco/images/test2017/'  # 图像
dst_img_path = './coco/images/test2017/'
cls_id = ['1', '2', '3', '5', '7', '8', '10', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '28', '39', '40', '51', '52', '75', '79']  # 替换后的序号列表

# 创建目标目录
os.makedirs(dst_img_path, exist_ok=True)

# 遍历图像文件
image_files = os.listdir(src_path)
image_files.sort()

for image_file in image_files:
    # 检查文件扩展名是否为图片格式
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        # 复制图像文件到目标目录
        src_image_path = os.path.join(src_path, image_file)
        dst_image_path = os.path.join(dst_img_path, image_file)
        print("Copying from:", src_image_path)
        print("Copying to:", dst_image_path)
        copyfile(src_image_path, dst_image_path)
