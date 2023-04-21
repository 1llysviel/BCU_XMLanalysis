import xml.sax
# 启动文档
def startDocument(self):
    print("******xml文件开始解析******")
# 开始解析xml
def startElement(self, name, attributes):
    self.tag = name
    # if name=="flaw"
    if name == "file":
            self.path = attributes["path"]
    if name=="testcase":
            self.id=attributes["id"]
            print(f"xml文件中id号为{self.id}对应的文件路径为：{self.path}")
            print(self.path)
# xml内容事件处理
    def characters(self, content):
        pass
    # 结束解析xml
    def endElement(self, name):
        pass
    # xml结束标签调用
    def endDocument(self):
        print("******xml文件解析结束******")
if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    Handler = ConfigHandler()
    parser.setContentHandler(Handler)
    # 解析 xml 这里可以写xml 的具体路径,为了简单放在了同一个文件夹里面了
    parser.parse("full_manifest.xml")