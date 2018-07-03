# coding=utf-8

from lexical_analysis import word_stream

#语法树，文法，非终结符
class noterminal(list):
    def __init__(self,l=[]):
        list.__init__([])
        self.extend(l)


#检测文法和句子是否匹配
#只考虑右递归
def grammar(t_noterminal, t_sentence):
    # 对此非终结符中每个文法
    for production in eval(t_noterminal):
        #当前文法词序号seq
        for sequence in range(0, len(production)):
            #当前文法当前词序号是非终结符
            if type(production[sequence]) is str:
                #当前词序到结尾的句子和当前词序代表的终结符进入递归
                #保存剩余句子
                t = t_sentence[sequence:]
                #当前句删除剩余句子
                t_sentence = t_sentence[:sequence]
                #检查结果,保存返回深一层子句list
                result = grammar(production[sequence], t)
                if result == False:
                    #当前句恢复子句
                    t_sentence.extend(t)
                    break
                    # return False
                else:
                    # 当前句子后加递归返回的深一层list包裹的return子句
                    t_sentence.append(result)
                    return t_sentence
            #文法和句子当前词sort相符
            elif production[sequence] == t_sentence[sequence][1]:
                #文法全部相符
                if sequence == len(t_sentence)-1:
                    return t_sentence
            else:
                if production is eval(t_noterminal)[-1]:
                    return False
                else:
                    break


#定义文法
#E=noterminal([([4,3]),grammar([5])])
#A=noterminal([([4,1,E])])
#S=noterminal([([1,4]),grammar([A])])
E=noterminal([[4],[5]])
A=noterminal([['E'],[4,3,'A']])
S=noterminal([[1,'E'],['A']])
tree=[]

#每句
current_word = 0
last_semicolon = 0
end_word = len(word_stream)-1
grammar_forest=[]
tree=[]
while True:
    if last_semicolon == len(word_stream):
        print('分析完成')
        break
    #循环从word_stream中取句子
    #this_semicolon,last_semicolon中间的句子入句子栈
    while True:
        print(word_stream[current_word][0])
        if word_stream[current_word][0] is ';':
            #删分号
            # last_semicolon += 1
            sentence = word_stream[last_semicolon:current_word]
            current_word += 1
            break
        current_word += 1
    tree = grammar('S', sentence)
    if tree is False:
        tree = '词句语法错误'
    grammar_forest.append(tree)
    last_semicolon = current_word

print('\ntree:\n',grammar_forest)


# print(tree)
