#5类词：
#定义关键字表:1
KeywordList = ['if','int','then','do','print']
#定义分界符表:2
DelimiterList = [';']
#定义运算符表(算术运算符和关系运算符):3
OperatorList = ['=','-','+','*','/','>','<']
#常数0,标识符4，
#单词栈
Word = ''
#输出流
OutStream = []


#判断是否为关键字，再一个循环，判断完此单词，
def IfKeyword(Char):
    pass

#取一个字符，判断属2/3否,判断0否,判断1否(根据表1构建最小DFA，入栈，),str和类型构成2元组，插入list，位置为循环计数
SourceCodeFile = open('./SourceCode','r')
num = True
sort = 1
FileEnd = False

while FileEnd == False:
    Char = SourceCodeFile.read(1)
    #文件结束
    if Char == '':
        SourceCodeFile.close()
        FileEnd = True
        break

    #重写，每次字符都入Word栈,循环开始

    #重写，检测到分隔符，根据sort（栈中种类）栈中元素加进OutStream,清栈,
    #运算式子之间，加空格: a = 1 + 1
    if Char == (' ' or '\n'):
        OutStream.append((Word,sort))
        Word = ''
        break


    Word += Char

    #种类检测，只设置sort，
    if Char in DelimiterList:
        sort = 2
        break

    if Char in OperatorList:
        sort = 3
        break

    #num==1:上一个char是数字

#    if num == True and Char.isdigit() == False:
#        OutStream.append((Word.pop(),0))
#        num = False


#数字后是字母，字母后是数字怎么解决？
    if Char.isdigit() == True:
        if num == True:
            num = True
            sort = 0
        break

    if IfKeyword(Char) == True:
        sort = 1
        break
    else:
        sort = 4
        break

SourceCodeFile.close()

OutFile = open('./OutFile','w')
#OutStream   list转换str  函数

OutFile.write(str(OutStream))

OutFile.close()

