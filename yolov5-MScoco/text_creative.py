import os

def generate_txt_file(image_dir, txt_file):
    with open(txt_file, 'w') as f:
        for filename in os.listdir(image_dir):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                f.write(os.path.join(image_dir, filename) + '\n')

# 指定数据集目录
train_image_dir = './coco/images/train2017/'
#test_image_dir = './coco/images/test2017/'
val_image_dir = './coco/images/val2017/'

# 生成 train.txt
generate_txt_file(train_image_dir, 'train2017.txt')

# 生成 test.txt
#generate_txt_file(test_image_dir, 'test-dev2017.txt')

# 生成 val.txt
generate_txt_file(val_image_dir, 'val2017.txt')
