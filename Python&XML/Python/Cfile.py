from importlib.resources import path
import os

#  ID:6

#  Name:CWE-416: Use After Free

#  Language: C

#  Path:000/000/006/Using_freed_memory.c

#  Line:['15', '12']

# ******************************************
Line = [] #log.txt已有
lines = []
lines.append(Line)
#需要循环读取log.txt中的Line数组内容，添加进lines

#思路2：仿照xml，循环def，每次重置

output_file = 'output.txt'

# with open('log2.txt', 'r', encoding="utf-8") as f:
#     paths = f.read().split()

#     for i in paths:
#         for path in paths:
#             for dirpath, _, filenames in os.walk(path): #遍历path中所有目录和子目录，返回当前目录地址，当前目录下所有子目录名称，当前目录下所有文件名称
#                 for filename in filenames:
#                     if filename.endswith('.c'):
#                         # 使用os.path.join()函数拼接路径和文件名
#                         file_path = os.path.join(dirpath, filename) #拼接目录路径和文件名称为完整路径
#                         with open(file_path, 'r') as f:
#                             Flines =f.readline()
#                             for l in lines[i]:
#                                 output_file.write(lines[l-1])

with open('log2.txt', mode= "r" , encoding= "utf-8") as input:
    path = input.read().split()
    for i,Path in input:
        if Path.endswith('.c'):
            test = Path
            print(test)
