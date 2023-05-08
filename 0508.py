import xml.sax
import pandas
line=[]    #用于纪录xml文件中的漏洞行信息

def source_file_prefix(path,prefix):
    with open(r'D:/source_file.txt', mode='a', encoding='utf-8') as s:  # 将源文件对应的文件对象命名为s
        new_path = prefix+ path
        with open(new_path, mode='r', encoding='utf-8') as r:  # 将路径对应文件的文件对象设置为r
                a = r.read()
                s.write(a)
                s.write("==============================\n")


def source_file(path):  #通过漏洞对应路径获取相应源文件
        try:
            source_file_prefix(path,'D:/Sard_archive/testcases/')
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            source_file_prefix(path, 'D:/Sard_archive/')


def line_file_prefix(path,line,prefix):
    with open('D:/line_file.txt', mode='a', encoding='utf-8') as l:  # 将漏洞文件对应的文件对象命名为s
        new_path = prefix + path
        with open(new_path, mode='r', encoding='utf-8') as r:  # 将路径对应文件的文件对象设置为r
                a = r.readlines()
                new_list = list(map(int, line))  # 将字符类型的列表转换为整型的列表
                for i in new_list:
                    l.write(a[i - 1].strip('\n'))  # i-1因为将文件内容保存数组中，但是数组的下标是从零开始
                l.write('\n==============================\n')


def line_file(path,line):  #通过漏洞对应路径获取相应源文件h
        try:
            line_file_prefix(path, line,'D:/Sard_archive/testcases/' )
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            line_file_prefix(path, line, 'D:/Sard_archive/')
            return
        except IndexError:
            pass

class ConfigHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.path = ""
        self.line = ""
        self.name = ""
        self.language = ""
        self.id = ""

    # 启动文档
    def startDocument(self):
        print("****************xml file parsing begins****************")

    # 开始解析x
    def startElement (self, lable, attributes):  #startElement(lable, attrs): 遇到XML开始标签时调用，lable是标签的名字，attributes是标签的属性值字典。
        global line
        if lable == "testcase":  # 在testcase标签里面查找语言类型
            self.language = attributes["language"]  # 获取源代码语言类型
            self.id = attributes["id"]  # 获取漏洞代码对应id号
        if lable == "file":
            self.path = attributes["path"]
        if lable=="flaw":
                self.name = attributes["name"]
                self.line = attributes['line']
                line.append(self.line)  #将获取到的漏洞所在行数追加到line列表中


    # 结束解析xml
    def endElement(self,name):   #endElement(name) : 遇到XML结束标签时调用
        global line
        if name == "testcase":  #表示一个id对应的段落读取完毕
             with open(r"D:\xml_file.txt", mode="a", encoding="utf-8") as log:  # 创建一个文件对象log，便于将读取的数据放入文件
                if self.line and self.id and self.path and line:   #如果缺陷行号不为空，那么就说明存在缺陷，既满足提取条件,并且源代码是用C语言或者c++书写，那么就获取对应路径和错误名称
                    if  self.language=="C" or self.language=="C++":
                            print(f'文件路径为：{self.path}')
                            source_file(self.path)  #将文件目录对应的文件内容写入D盘符source_file文件中
                            line_file(self.path,self.line)
                            print(f"id:{self.id} \nlanguage:{self.language}\nname：{self.name}\npath：{self.path}\nline:{line}",file=log)
                            line.clear()  #每次将漏洞行数信息写入列表后，将列表内容初始化，从而不会影响后期漏洞行的写入
                            self.id=None
                            self.path=None
                            self.line=None
                            print("=============================",file=log)
                    else:    #因为当漏洞行数没有写入文件时候，读取的漏洞行依然会追加到列表中，所以要清空不满足条件的漏洞行数
                        line.clear()

    # xml结束标签调用
    def endDocument(self):
        print("*****************xml file parsing is complete*****************")


if __name__ == "__main__":
    parser = xml.sax.make_parser()      #这行代码创建了一个SAX解析器对象，用于解析XML文件
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)   #设置解析器的特性，使其不使用命名空间。
    Handler = ConfigHandler()          #创建一个ConfigHandler对象(自定义的类)，用于处理解析器解析XML文件时的事件。
    parser.setContentHandler(Handler)  #设置解析器的内容处理器为ConfigHandler对象。
    parser.parse("full_manifest.xml") #解析器解析指定的XML文件

