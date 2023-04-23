flage=True  #用于实现文件清空

def clear_file(filename):
    global flage
    if flage == True:
        filename.truncate(0)
        flage = False

def source_file(path):  #通过漏洞对应路径获取相应源文件
    with open(r'log2.txt',mode='a',encoding='utf-8') as source:  #将源文件对应的文件对象命名为source
        clear_file(source)
        # new_path='D:/Sard_archive/testcases/'+path
        new_path=path
        try:
         with open(new_path,mode='r',encoding='utf-8') as route:  #将路径对应文件的文件对象设置为r
            add=route.read()
            source.write(add)
            source.write("==============================\n")
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            print("share开头的文件目录不存在")
            return

def line_file(path,line):  #通过漏洞对应路径获取相应源文件
    with open(r'line_file.txt',mode='a',encoding='utf-8') as l:  #将漏洞文件对应的文件对象命名为s
        clear_file(l)
        new_path='D:/Sard_archive/testcases/'+path
        try:
          with open(new_path,mode='r',encoding='utf-8') as r:  #将路径对应文件的文件对象设置为r
                a=r.readlines()
                new_list=list(map(int,line))  #将字符类型的列表转换为整型的列表
                for i in new_list :
                     print(a[i-1].strip('\n'))   #i-1因为将文件内容保存数组中，但是数组的下标是从零开始
                     l.write(a[i-1].strip('\n'))
                l.write('\n==============================')
                l.write('\n')
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            print("share开头的文件目录不存在")
            return
        except IndexError:
            print("漏洞行数少于源文件行数")
            return