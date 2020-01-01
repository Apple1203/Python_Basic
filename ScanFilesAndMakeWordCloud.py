import wordcloud

import os

import re

import collections # 词频统计库

import numpy as np

from PIL import Image # 图像处理库

import matplotlib.pyplot as plt

import matplotlib

def scan_files(directory, prefix=None, postfix='.py'):

    """
    参数directory表示目录名，prefix和postfix是目录的前后缀，默认是没有的
    该函数可以循环扫描directory目录及其子目录下所有的文件，以列表形式返回
    """

    files_list = []

    for root, sub_dirs, files in os.walk(directory):

        for special_file in files:

            if postfix:

                if special_file.endswith(postfix):

                    files_list.append(os.path.join(root, special_file))

            elif prefix:

                if special_file.startswith(prefix):

                    files_list.append(os.path.join(root, special_file))

            else:

                files_list.append(os.path.join(root, special_file))

    return files_list



# 读取当前目录的上级目录
temp = os.path.abspath('D://王明灏//seu//2019//Python//iseu2012-python2019-master//python2019')


# 应用示例
all_files = scan_files(temp)

cloud = wordcloud.WordCloud()

txt=''

for i in all_files:

  file=open(i,encoding='UTF-8')

  txt=txt+file.read()

list=re.findall('[a-zA-Z]+',txt)#接收所有纯英文的单词


# 词频统计

word_counts = collections.Counter(list) # 对分词做词频统计

word_counts_top10 = word_counts.most_common(10) # 获取前10最高频的词

print (word_counts_top10) # 输出检查

# 词频展示

cloud.generate_from_frequencies(word_counts) # 从字典生成词云

cloud.to_file('D://王明灏//seu//2019//Python//happy.jpg')

# 直方图展示高频词汇

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

common_name = [x[0] for x in word_counts_top10] # 高频词汇列表

common_value = [x[-1] for x in word_counts_top10] # 高频词汇出现次数列表

plt.bar(common_name, common_value, width=0.5) # 柱状图设置

plt.savefig('D://王明灏//seu//2019//Python//bar.jpg',dpi=1000)
