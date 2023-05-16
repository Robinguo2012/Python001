import os
import shutil
import json

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print('create path: {}'.format(path))


# 创建文件，写入一行
# 文件夹
folder = os.getcwd() + '/test'
# 文件
file = folder + '/test.txt'

def write_file():
    if os.path.exists(folder):
        print('remove folder: {}'.format(folder))
        shutil.rmtree(folder)

    mkdir(folder)
    
    name = input('请输入姓名:').strip()
    age = input('请输入年龄:').strip()

    with open(file, 'w+', encoding='utf-8') as f:
        f.write('姓名：{}\n'.format(name))
        f.write('年龄：{}\n'.format(age))


def read_file():
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(line.strip())


def write_json():
    sample = '[1, "simple", "list"]'
    with open(folder + '/test.json', 'w+', encoding='utf-8') as f:
        json.dump(sample, f)


# write_file()
# read_file()
write_json()



