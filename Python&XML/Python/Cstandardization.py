import re

def Standardization(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # 删除注释和空格
            line = re.sub(r'\/\/.*|\/\*.*?\*\/|\s+', '', line) #正则表达式过滤注释等
            # 写入输出文件
            if line:
                output_file.write(line)

input_file_path = 'Format_string_problem.c' #输入文件路径
output_file_path = 'output.c' #输出文件路径
Standardization(input_file_path, output_file_path)


