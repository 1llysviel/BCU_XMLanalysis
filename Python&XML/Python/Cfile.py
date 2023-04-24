Point = True

def clear_file(filename):
    global Point
    if Point ==True:
        filename.truncate(0)
        Point = False

def source_file(path):
    with open(r'source_file.txt',mode='a',encoding='utf-8') as source:
        clear_file(source)
        source_code = path
        try:
            with open(source_code,mode='r',encoding='utf-8') as resource:
                add = resource.read()
                source.write(add)
                source.write("========================================\n")
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            print("未找到路径所在文件")
            return

def line_file(path,line):
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

def output_line(line):
    print(f"漏洞对应行数：",end='')
    for i in range(len(line)):
        if i == len(line)-1:
            print(line[i])
        else:
            print(line[i],end=",")