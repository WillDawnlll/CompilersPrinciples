#5类词：
#定义关键字表:1
KeywordList=['if','where','elesif','int','do','return']
#定义分界符表:2
DelimiterList=['"','{','}','(',')']
#定义运算符表(算术运算符和关系运算符):3
OperatorList=['=','-','+','*','/','>','<']
#标识符5，常数0

#取一个字符，判断属2/3否,判断0否,判断1否(根据表1构建最小DFA，入栈，),str和类型构成2元组，插入list，位置为循环计数
SourceCodeFile=open('./SourceCode','r')
FileEnd=0

while FileEnd!=1:
    Char=SourceCodeFile.read(1)

    #文件结束
    Char为空时
    FileEnd=1


    IfDelimiter(Char)
    IfOperator(Char)
    IfNumber(Char)




