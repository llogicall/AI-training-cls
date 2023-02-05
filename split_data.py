import os
import sys
import shutil
import numpy

def load_data(data_path):  
    # 将硬盘中的数据读取到内存中
    count = 0
    data = {}  #字典
    for dir_name in os.listdir(data_path): #遍历获取data_path目录下的所有文件
        dir_path = os.path.join(data_path, dir_name)
        

def copy_dataset(src_img_list, data_index, target_path):
    target_img_list = []

def write_file(data,file_name):

def split_data(src_data_path, target_data_path, train_rate=0.8):

def main():
    src_data_path = sys.argv[1]

if __name__ == "__main__":
    main()

