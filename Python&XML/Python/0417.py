#  ID:6

#  Name:CWE-416: Use After Free

#  Language: C

#  Path:000/000/006/Using_freed_memory.c

#  Line:['15', '12']

# ******************************************

TPath = []
Tline = []
i = 0

# txt信息提取
def TxTinf():
    global i
    with open('log2.txt', 'r') as f:
        for txt in f:
            if 'Line:' in txt: #查找txt内的Line
                line = txt.strip().split(':')[1].strip() #去除前后空格并以‘：’切分提取
                Tline.append(line) #添加到总数组

            if 'Path:' in txt: #查找txt内的Path
                path = txt.strip().split(':')[1].strip()
                TPath.append(path)

                file = open(TPath[i], mode='r', encoding='utf-8') #顺序打开路径
                C_code = file.readline() #读取行
                content =C_code[Tline[i]] #利用传参按顺序读取行
                i = i+1
                print(content)
                print(Tline)
                print("*******************")
                file.close()

                # for line_num, line in enumerate(C_code):
                    # if line_num in

# .c&.cpp内容提取
# def Content():

TxTinf()
# print(Path)