from xml import sax
line = []
point = False

#  ID:74

#  Name:CWE-389: Error Conditions, Return Values, Status Codes

#  Language: C

#  Path:000/000/074/Ignored_function_return_value.c

#  Line:['3', '0']

# ******************************************

# 199231 231334 148966 149042

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


        if label == "file":
            self.path = attrs["path"]


        if label == "flaw":
            point = True
            self.line = attrs["line"]
            line.append(self.line)
            self.name = attrs["name"]


    def endElement(self,label):

        global point

        # with open(r"D:\0.Network&Security\log.txt", mode="a", encoding="utf-8") as log:
        with open(r'log.txt', mode="a", encoding="utf-8") as log:
            if label == "testcase":
                if self.language == "C" or self.language == "C++":
                    if point == True:
                        # print(f" ID:{self.id} \n",file=log)
                        # print(f" Name:{self.name} \n",file=log)
                        # print(f" Language:",self.language," \n",file=log)
                        # # 加入file的endelement判断哪个是源文件
                        # print(f" Path:{self.path} \n",file=log)
                        # print(f" Line:{line} \n",file=log)
                        # print(f"****************************************** \n",file=log)

                        print(f" ID:{self.id} \n")
                        print(f" Name:{self.name} \n")
                        print(f" Language:",self.language," \n")
                        # 加入file的endelement判断哪个是源文件
                        print(f" Path:{self.path} \n")
                        # for i in range(len(line)):
                        print(f" Line:{line} \n")
                        print(f"****************************************** \n")

                        self.id = ""
                        self.language = ""
                        self.path = ""
                        self.line = ""
                        self.name = ""
                        point = False
                        line.clear()


    def charaters(self,content):
        pass

if __name__ == "__main__":

    handler = CWEHandler()
    # sax.parse("D:/0.Network&Security/Python&XML/Python/less_manifest.xml",handler)
    # sax.parse('full_manifest.xml',handler)
    sax.parse('less_manifest.xml',handler)