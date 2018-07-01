# coding=utf-8

from lexical_analysis import word_stream

# print(WordStream)
#
# for a in WordStream:
#     print(type(a))


# 测试 单句语法分析
# A = 'a = a * b + c ;'
# class SyntaxTree(object):
#     pass

# 文法类的list构建语法子树的函数（是否作为语法树类的方法？）


# 文法类：
# 成员为导出式
# 方法为判断是否为此文法
# class Grammar(object):
#     def __init__(self,grammar):
#         self.grammar = grammar
#     def
#序号
class tree(list):
    def __init__(self,l):
        self.list=l
class grammer(list):
    def __init__(self,l):
        self.list=l
class noterminal(list):
    def __init__(self,g):
        self.gra=[]
        self.gra.append(g)


#检测文法和句子是否匹配
def right(t_grammer, t_sentence):
    for seq in range(0, len(t_grammer) - 1):
        #当前单词为非终结符,递归,检测此非终结符和剩余句子
        if t_grammer[seq] is list:
            #此非终结符替换为相应子句
            t_grammer[seq] = right(t_grammer[seq], t_sentence[seq:-1])
        else:
            if t_sentence[seq][1] == t_grammer[seq]:
                if seq == len(t_grammer)-1:
                    return t_sentence
            else:
                global num
                print('第%s行出错\n'%num)
                return False




current_word = 0
last_semicolon = 0
end_word = len(word_stream)-1
while True:
    if current_word == len(word_stream)-1:
        print('分析完成')
        break
    #循环从word_stream中取句子
    #this_semicolon,last_semicolon中间的句子入句子栈
    while True:
        current_word += 1

        if word_stream[current_word][0] is ';':
            current_word += 1
            sentence = word_stream[last_semicolon:current_word]
            break
    print(sentence)

    #根据首词sort选文法
    E=noterminal([[4,3],5])
    A=noterminal([[4,1,E]])
    # 列表实现节点分叉不固定树
    S=noterminal([[1,4],A])

    tree = right(A,sentence)
    


    #调用当前文法判断函数：(多文法用一个程序？文法存在list中,0为非终结符)
    #符合，构建语法树当前节点用此文法扩展子树
    #不符，打印行数，输出语法错误提示,return False



    last_semicolon = current_word


# print(tree)
