#5类词：
#定义关键字表:1
KeywordList = ['if','int','then','do','print']
#定义分界符表:2
DelimiterList = [';']
#定义运算符表(算术运算符和关系运算符):3
OperatorList = ['=','-','+','*','/','>','<']
#常数0,标识符5，
#单词栈
Word = []
#输出流
OutStream = []

def IfKeyword():

    pass

#取一个字符，判断属2/3否,判断0否,判断1否(根据表1构建最小DFA，入栈，),str和类型构成2元组，插入list，位置为循环计数
SourceCodeFile = open('./SourceCode','r')
FileEnd = 0
SequenceNumber = 5

while FileEnd == 0:
    Char = SourceCodeFile.read(1)
    #文件结束
    if Char == '':
        FileEnd = 1
        SourceCodeFile.close()
        break
    if Char == (' ' or '\n'):
        break

    if Char in DelimiterList:
        OutStream.append((Char,2))
        break

    if Char in OperatorList:
        OutStream.append((Char,3))
        break

    #num:上一个char是数字

    if num == 1 and Char.isdigit() == fause:
        OutStream.append(Tuple(Word.pop(),0))
        num = 0

    Word.append(Char)


    if Char.isdigit() == true:
        num = 1
        break

    if IfKeyword(Char) == 0:
        OutStream.append(Tuple(Word.pop(),5))
        break

SourceCodeFile.close()

OutFile = open('./OutFile','w')
#OutStream   list转换str  函数

OutFile.write(str(OutStream))

OutFile.close()

