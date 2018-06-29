# coding=utf-8
# 5类词
# 定义关键字表:1
KeywordList = ['if', 'int', 'then', 'do', 'print', 'return']
# 定义分界符表:2
DelimiterList = [';']
# 定义运算符表(算术运算符和关系运算符):3
OperatorList = ['=', '-', '+', '*', '/', '>', '<']
# 常量5,标识符4，无类别为0
# 单词栈
Word = ''
# 输出流
WordStream = []


# 判断是否为关键字，再一个循环，判断完此单词，
def if_keyword(char):
    for w in KeywordList:
        for r in w:
            if char == r:
                if r == w[-1]:
                    global Word
                    Word = w
                    return True
                else:
                    Word += char
                    char = SourceCodeFile.read(1)
    return False


# 取一个字符，判断属2/3否,判断5否,判断1否(根据表1构建最小DFA，入栈，),str和类型构成2元组，插入list，位置为循环计数
SourceCodeFile = open('./SourceCode', 'r')
num = True
sort = 0

while True:
    Char = SourceCodeFile.read(1)
    # 文件结束
    if Char == '':
        SourceCodeFile.close()
        break

    # 重写，每次字符都入Word栈,循环开始

    # 重写，检测到分隔符，根据sort（栈中种类）栈中元素加进OutStream,清栈,
    # 运算式子之间，加空格: a = 1 + 1
    if Char == (' ' or '\n'):
        WordStream.append((Word, sort))
        Word = ''
        continue

    Word += Char

    # 种类检测，只设置sort，
    if Char in DelimiterList:
        sort = 2
        continue

    if Char in OperatorList:
        sort = 3
        continue

    # num==1:上一个char是数字

    #    if num == True and Char.isdigit() == False:
    #        OutStream.append((Word.pop(),0))
    #        num = False

    # 数字后是字母，字母后是数字怎么解决？
    if Char.isdigit():
        if num:
            num = True
            sort = 5
        continue

    if if_keyword(Char):
        sort = 1
        continue
    else:
        sort = 4
        continue

SourceCodeFile.close()

OutFile = open('./OutFile', 'w')
# OutStream   list转换str  函数

OutFile.write(str(WordStream))

OutFile.close()
