# 从coco128中提取车类的image和label
# 0 bicycle
# 1 car
# 2 motorcycle
# 3 bus
# 4 truck

import os
from shutil import copyfile

src_path = 'F:/datasets/coco/images/val2017/'  # 图像
img_path = 'F:/datasets/coco/labels/val2017/'  # 标签
dst_label_path = './coco/labels/val2017/'
dst_img_path = './coco/images/val2017/'
cls_id = ['1', '2', '3', '5', '7', '8', '10', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '28', '39', '40', '51', '52', '75', '79']  # 替换后的序号列表


labels = os.listdir(img_path)
labels.sort()

# 创建目标目录
os.makedirs(dst_label_path, exist_ok=True)
os.makedirs(dst_img_path, exist_ok=True)

for label in labels:
    if label[-1] != 't':
        continue
    # 存标签
    tmp = []
    for line in open(img_path + label):
        str_list = line.split()
        # 被选类别的标签
        for i in range(len(cls_id)):
            if str_list[0] == cls_id[i]:
                # 改成自己的标签，这里是数组下标
                line = str(i) + line[1:]
                tmp.append(line)
    # 没有被选类别
    if len(tmp) < 1:
        continue
    # 新的标签文件
    with open(dst_label_path + label, 'w') as f:
        for item in tmp:
            f.write(item)
    image = label[:-4] + '.jpg'
    src_image_path = src_path + image
    dst_image_path = dst_img_path + image
    print("Copying from:", src_image_path)
    print("Copying to:", dst_image_path)
    # 检查文件是否存在
    if os.path.exists(src_image_path):
        # 拷贝有被选类别的图片
        copyfile(src_image_path, dst_image_path)
    else:
        print("Warning: File", src_image_path, "not found. Skipping...")
