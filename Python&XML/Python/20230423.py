import xml.sax
line=[]
flage=True  #用于实现文件清空

def clear_file(filename):
    global flage
    if flage == True:
        filename.truncate(0)
        flage = False

def source_file(path):  #通过漏洞对应路径获取相应源文件
    with open(r'source_file.txt',mode='a',encoding='utf-8') as s:  #将源文件对应的文件对象命名为s
        clear_file(s)
        new_path=path
        try:
         with open(new_path,mode='r',encoding='utf-8') as r:  #将路径对应文件的文件对象设置为r
            a=r.read()
            s.write(a)
            s.write("==============================\n")
        except UnicodeDecodeError:
            print("无法找到正确的打开文件编码格式")
            return
        except FileNotFoundError:
            print("share开头的文件目录不存在")
            return

def line_file(path,line):  #通过漏洞对应路径获取相应源文件
    with open(r'line_file.txt',mode='a',encoding='utf-8') as l:  #将漏洞文件对应的文件对象命名为s
        clear_file(l)
        new_path=path
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

def  print_line(line):  #将漏洞列表中元素进行输出，并用逗号进行隔开，方便分析代码
    print(f"漏洞对应行数:",end='')
    for i in range(len(line)) :
        if i == len(line)-1:
            print(line[i])
        else:
            print(line[i],end=",")

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

    def characters(self, content):
        pass

    # 结束解析xml
    def endElement(self,name):   #endElement(name) : 遇到XML结束标签时调用
        global line
        if name == "testcase":  #表示一个id对应的段落读取完毕
             with open(r'xml_file.txt', mode="a", encoding="utf-8") as log:  # 创建一个文件对象log，便于将读取的数据放入文件
                clear_file(log)
                if self.line and self.id and self.path :   #如果缺陷行号不为空，那么就说明存在缺陷，既满足提取条件,并且源代码是用C语言或者c++书写，那么就获取对应路径和错误名称
                    if  self.language=="C" or self.language=="C++":
                            print(f'文件路径为：{self.path}')
                            source_file(self.path)  #将文件目录对应的文件内容写入D盘符source_file文件中
                            line_file(self.path,self.line)
                            print(f"id:{self.id} \nlanguage:{self.language}\nname:{self.name}\npath:{self.path}\nline:{line}",file=log)
                            self.id=None
                            self.path=None
                            self.line=None
                            line.clear()  #每次将漏洞行数信息写入列表的前，将列表内容初始化
                            print("=============================",file=log)
    # xml结束标签调用
    def endDocument(self):
        print("*****************xml file parsing is complete*****************")


if __name__ == "__main__":
    parser = xml.sax.make_parser() #这行代码创建了一个SAX解析器对象，用于解析XML文件
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = ConfigHandler()
    parser.setContentHandler(Handler)
    # 解析 xml 这里可以写xml 的具体路径,为了简单放在了同一个文件夹里面了
    parser.parse('less_manifest.xml')
    # parser.parse('full_manifest.xml')

