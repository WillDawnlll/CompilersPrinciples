#5类词：
#定义关键字表:1
KeywordList=['if','where','elesif','int','do','return']
#定义分界符表:2
DelimiterList=['"','{','}','(',')']
#定义运算符表(算术运算符和关系运算符):3
OperatorList=['=','-','+','*','/','>','<']
#常数0,标识符5开始增，
#单词栈
Word=[]

def IfDelimiter():
    pass

def IfOperator(Char):
    pass

def IfNumber():
    pass

def IfKeyword():
    pass

def RecordKeyword():
    SequenceNumber+=1
    pass

#取一个字符，判断属2/3否,判断0否,判断1否(根据表1构建最小DFA，入栈，),str和类型构成2元组，插入list，位置为循环计数
SourceCodeFile=open('./SourceCode','r')
FileEnd=0

while FileEnd==0:
    Char=SourceCodeFile.read(1)
    #文件结束
    if Char=='':
        FileEnd=1
        SourceCodeFile.close()
        break


    IfDelimiter(Char)
    IfOperator(Char)
    IfNumber(Char)
    IfKeyword(Char)

    SequenceNumber=5
    RecordKeyword()

SourceCodeFile.close()


