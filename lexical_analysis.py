# coding=utf-8
# 5类词
# 定义关键字表:1
keyword = ['if', 'int', 'then', 'print', 'return']
# 定义分界符表:2
delimiter = [';']
# 定义运算符表(算术运算符和关系运算符):3
operator = ['=', '-', '+', '*', '/', '>', '<']
# 常量5,标识符4，无类别为0
# 省略符号表
omit_char = [' ', '\n']
# 单词栈
word = ''
# 输出流
word_stream = []


def next_char():
    global word, char
    word += char
    char = source_code.read(1)
    return char

#dfa
def is_keyword():
    global char, word
    if char is 'i':
        return i()
    elif char is 't':
        return t()
    elif char is 'p':
        return p()
    elif char is 'r':
        return r()
    else:
        next_char()
        return False


def i():
    next_char()

    if char is 'n':
        return n()
    elif char is 'f':
        return f()
    elif char is ' ':
        return True
    else:
        return False


def t():
    next_char()
    if char is 'h':
        return h()
    elif char is 'u':
        return u()
    elif char is ' ':
        return True
    else:
        return False


def p():
    next_char()
    if char is 'r':
        return r()
    else:
        return False


def r():
    next_char()
    if char is 'e':
        return e()
    elif char is 'i':
        return i()
    else:
        return False


def n():
    next_char()
    if char is 't':
        return t()
    elif char is ' ':
        return True
    else:
        return False


def h():
    next_char()
    if char is 'e':
        return e()
    else:
        return False


def u():
    next_char()
    if char is 'r':
        return r()
    else:
        return False


def e():
    next_char()
    if char is 'n':
        return n()
    else:
        return False


def f():
    next_char()
    if char is ' ':
        return True
    else:
        return False

#有错，改为dfa
# 判断是否为关键字，再一个循环，判断完此单词，
# def if_keyword(char):

# id = ''
# for w in KeywordList:
#     for r in w:
#         if next_char() is r:
#             if r == w[-1]:
#                 global Word
#                 Word = w
#                 return True
#             else:
#                 id += char
#                 char = SourceCodeFile.read(1)
# Word = id
# return False


source_code = open('./source_code', 'r')
sort = 0
char = source_code.read(1)
while True:
    # 文件结束
    if char is '':
        source_code.close()
        break

    if char in omit_char:
        word_stream.append((word, sort))
        word = ''
        char = source_code.read(1)
        continue

    # 种类检测，设置sort
    if char in delimiter:
        sort = 2
        next_char()
    elif char in operator:
        sort = 3
        next_char()
    elif char.isdigit():
        sort = 5
        next_char()
    elif is_keyword():
        sort = 1
    else:
        sort = 4

source_code.close()

output_file = open('./output', 'w')
output_file.write(str(word_stream))
output_file.close()
