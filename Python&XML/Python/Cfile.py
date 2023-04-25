Point = True

def clear_file(filename):
    global Point
    if Point ==True: # 如果Point为True，则执行清空文件操作，否则跳过
        filename.truncate(0)
        Point = False

def source_file(path):
    with open(r'source_file.txt',mode='a',encoding='utf-8') as source: #将源文件对应的文件对象命名为source
        clear_file(source) # 调用清空文件函数，清空文件
        source_code = path
        try:
            with open(source_code,mode='r',encoding='utf-8') as resource: #将路径对应文件的文件对象设置为resource
                add = resource.read()
                source.write(add)
                source.write("========================================\n")
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            print("未找到路径所在文件")
            return

def line_file(path,line): #通过漏洞对应路径获取相应源文件
    with open(r'line_file.txt',mode='a',encoding='utf-8') as LineNum:
        clear_file(LineNum)
        source_line = path
        try:
            with open(source_line,mode='r',encoding='utf-8') as resource:
                add = resource.readlines()
                new_list = list(map(int,line))
                for i in new_list:
                    print(add[i-1].strip('\n'))
                    LineNum.write(add[i-1].strip('\n'))
                LineNum.write("========================================\n")
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            print("未找到路径所在文件")
            return
        except IndexError:
            print("漏洞行数少于源文件行数")
            return

def output_line(line): #将漏洞列表中元素进行输出，并用逗号进行隔开，方便分析代码
    print(f"漏洞对应行数：",end='')
    for i in range(len(line)):
        if i == len(line)-1:
            print(line[i])
        else:
            print(line[i],end=",")

# clear_file(log)
# source_file(self.path)  #将文件目录对应的文件内容写入D盘符source_file文件中
# line_file(self.path,self.line)