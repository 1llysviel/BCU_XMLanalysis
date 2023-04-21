from xml import sax
line = []
point = False

class CWEHandler(sax.ContentHandler):
    def __init__(self):
        sax.ContentHandler.__init__(self)
        self._content = ""
        self._tag = ""
        self.path = ""
        self.description = ""
        self.language = ""
        self.line = ""
        self.name = ""

    def startElement(self,label,attrs): # <testcase id="3"
        self._tag = label
        global point

        if label == "testcase":
            self.id = attrs["id"]
            self.language = attrs["language"]
            # if point == True:
                # print(f" ID:{self.id} \n")

        if label == "file":
            self.path = attrs["path"]
            # if point ==True:
                # print(f" Path:{self.path} \n")

        if label == "flaw":
            point = True
            self.line = attrs["line"]
            line.append(self.line)
            self.name = attrs["name"]
            # if point == True:  #每次将漏洞行数信息写入列表的前，将列表内容初始化
                # print(f" Line:{self.line} \n")
                # print(f" Name:{self.name} \n")
                # print(f" ID:{self.id} \n")
                # print(f" Path:{self.path} \n")
            #     point = False

    def endElement(self,label):

        global point

        with open(r'log.txt', mode="a", encoding="utf-8") as log:

            if label == "testcase":
                if self.language == "C" or self.language == "C++":
                    if point == True:
                        # print(f" ID:{self.id} \n",file=log)
                        # print(f" Name:{self.name} \n",file=log)
                        # print(f" Language:",self.language," \n",file=log)
                        # # 加入file的endelement判断哪个是源文件
                        # print(f" Path:{self.path} \n",file=log)
                        # for i in range(len(line)):
                        #     print(f" Line:{line} \n",file=log)
                        # print(f"****************************************** \n",file=log)

                        print(f" ID:{self.id} \n")
                        print(f" Name:{self.name} \n")
                        print(f" Language:",self.language," \n")
                        # 加入file的endelement判断哪个是源文件
                        print(f" Path:{self.path} \n")
                        # for i in range(len(line)):
                        print(f" Line:{line} \n")
                        print(f"****************************************** \n")

                        self.id = self._content
                        self.language = self._content
                        self.path = self._content
                        self.line = self._content
                        self.name = self._content
                        point = False
                        line.clear()
            # if label == "testcase":
            #     if  self.line and self.id and self.path:
            #         print("ID:",self.id,"\n")
            #         print("Path:",self.path,"\n")
            #         print("Language:",self.language,"\n")
            #         print("Line:",self.line,"\n")
                # print("test")

    def charaters(self,content):
        self._content = content

if __name__ == "__main__":

    handler = CWEHandler()
    sax.parse('less_manifest.xml',handler)