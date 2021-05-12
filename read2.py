import torch
import matplotlib.pyplot as plt
import os
import torch.nn as nn
import torch.autograd.variable as Variable
import numpy as np
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#定义读取文件下的所有文件函数
def find_all_files(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    return files

#定义读取数据函数
def read_datas(path):
    with open(data_path, 'r') as f:
        data_list = f.readlines() #将每一行读取为
        # print(data_list)
        data_list = [i.split('\n')[0] for i in data_list]   #因为这个\n是在每行数据最后，所以split后分为第一个数字串和第二个空串，所以[0]
        #print(data_list)
        data_list = [i.split('\t') for i in data_list]
        #print(data_list)  
        data = [(float(i[0]), float(i[1])) for i in data_list]   #将字符转换为float
        # print(data) 
        # test = input() 
    return data

#定义画图函数
def draw_pic(data, fish, fish_raman, data_file):
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    #对y值 min-max标准化
    y_max = max(y)
    y_min = min(y)
    y = [(i-y_min) / (y_max - y_min) for i in y]
    #定义x轴的范围
    #plt.xlim(min(x), max(x)) #注意，因为我们这里的数据非常规范，每个文件都是相同的x轴，所就没有求整体x的最值了（即任一一个都可以代替整体）
    #定义y轴的范围
    plt.ylim(0, 1)
    plt.plot(x, y, 'r-')
    # plt.show()
    subname = fish
    pic_name = fish_raman
    pic_num = ''.join(filter(lambda x: x, data_file[0:-4]))
    name='picture/' + subname + '/' +  pic_name + '-' +  pic_num#保存文件路径
    isExists = os.path.exists('picture/' + subname)
    if not isExists:
        os.makedirs('picture/' + subname)
    # print("name: ", name)
    plt.savefig(name)
    plt.cla()

path = "./data"#文件夹目录

#获得所有鱼的文件夹名
fishes_files = find_all_files(path) 
#['baijinqiang', 'danmaiwei', 'danmaizhong', 'diaoyu', 'dieyu', 'hongzun', 'nuowei', 'nuozhong', 'yinxueyu', 'zhiwei', 'zhizhong']

for fish in fishes_files:
    fish_inner_path = path + '\\' + fish #构造绝对路径，"\\"，其中一个'\'为转义符
    fish_num_files = find_all_files(fish_inner_path)
    #['1-1', '1-2', '2-1', '2-2', '3-1', '3-2']
    for fish_raman in fish_num_files:
        fish_raman_path = fish_inner_path + '\\' + fish_raman
        fish_data_files = find_all_files(fish_raman_path)
        #['1.txt', '2.txt', '3.txt', '4.txt', '5.txt'.......]
        for data_file in fish_data_files:
            data_path = fish_raman_path + '\\' + data_file
            #调用数据读取函数，获取每个拉曼txt文件夹中的拉曼数据
            data = read_datas(data_path) 
            #调用画图函数，进行画图, 同时传入鱼的名字,与编号
            draw_pic(data, fish, fish_raman, data_file)
            

