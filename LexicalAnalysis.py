# coding=utf-8
# 5类词
# 定义关键字表:1
KeywordList = ['if', 'int', 'then', 'print', 'return']
# 定义分界符表:2
DelimiterList = [';']
# 定义运算符表(算术运算符和关系运算符):3
OperatorList = ['=', '-', '+', '*', '/', '>', '<']
# 常量5,标识符4，无类别为0
# 省略符号表
OmitList = [' ', '\n']
# 单词栈
Word = ''
# 输出流
WordStream = []


def next_char():
    global Word, Char
    Word += Char
    Char = SourceCodeFile.read(1)
    return Char

#dfa
def keyword():
    global Char, Word
    if Char == 'i':
        return i()
    elif Char == 't':
        return t()
    elif Char == 'p':
        return p()
    elif Char == 'r':
        return r()
    else:
        next_char()
        return False


def i():
    char = next_char()
    if char == 'n':
        return n()
    elif char == 'f':
        return f()
    elif char == ' ':
        return True
    else:
        return False


def t():
    char = next_char()
    if char == 'h':
        return h()
    elif char == 'u':
        return u()
    elif char == ' ':
        return True
    else:
        return False


def p():
    char = next_char()
    if char == 'r':
        return r()
    else:
        return False


def r():
    char = next_char()
    if char == 'e':
        return e()
    elif char == 'i':
        return i()
    else:
        return False


def n():
    char = next_char()
    if char == 't':
        return t()
    elif char == ' ':
        return True
    else:
        return False


def h():
    char = next_char()
    if char == 'e':
        return e()
    else:
        return False


def u():
    char = next_char()
    if char == 'r':
        return r()
    else:
        return False


def e():
    char = next_char()
    if char == 'n':
        return n()
    else:
        return False


def f():
    char = next_char()
    if char == ' ':
        return True
    else:
        return False

#有错，改为dfa
# 判断是否为关键字，再一个循环，判断完此单词，
# def if_keyword(char):

# id = ''
# for w in KeywordList:
#     for r in w:
#         if char == r:
#             if r == w[-1]:
#                 global Word
#                 Word = w
#                 return True
#             else:
#                 id += char
#                 char = SourceCodeFile.read(1)
# Word = id
# return False


SourceCodeFile = open('./SourceCode', 'r')
sort = 0
Char = SourceCodeFile.read(1)

while True:
    # 文件结束
    if Char == '':
        SourceCodeFile.close()
        break

    if Char in OmitList:
        WordStream.append((Word, sort))
        Word = ''
        Char = SourceCodeFile.read(1)
        continue

    # 种类检测，设置sort
    if Char in DelimiterList:
        sort = 2
        next_char()
    elif Char in OperatorList:
        sort = 3
        next_char()
    elif Char.isdigit():
        sort = 5
        next_char()
    elif keyword():
        sort = 1
    else:
        sort = 4

SourceCodeFile.close()

OutFile = open('./OutFile', 'w')
OutFile.write(str(WordStream))
OutFile.close()
