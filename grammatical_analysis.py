# coding=utf-8

from lexical_analysis import word_stream

#语法树，文法，非终结符
class noterminal(list):
    def __init__(self,l=[]):
        list.__init__([])
        self.extend(l)


#检测文法和句子是否匹配
#只考虑右递归
def right(t_noterminal, t_sentence):
    # 对此非终结符中每个文法
    for tt_grammar in t_noterminal:
        #当前文法词序号seq
        for seq in range(0, len(tt_grammar) - 1):
            #当前文法当前词序号是非终结符
            if tt_grammar[seq] is noterminal:
                #当前词序到结尾的句子和当前词序代表的终结符进入递归
                #保存剩余句子
                tt_sentence = t_sentence[seq:-1]
                #当前句删除剩余句子
                t_sentence.pop(seq,-1)
                #检查结果,保存返回深一层子句list
                result = right(tt_grammar[seq], tt_sentence)
                if result == False:
                    return False
                else:
                    # 当前句子后加递归返回的深一层list包裹的return子句
                    return t_sentence.append(result)
            #文法和句子当前词sort相符
            elif tt_grammar[seq] == t_sentence[seq][1]:
                #文法全部相符
                if seq == len(t_noterminal)-1:
                    return t_sentence
                else:
                    return False


#定义文法
#E=noterminal([grammar([4,3]),grammar([5])])
#A=noterminal([grammar([4,1,E])])
#S=noterminal([grammar([1,4]),grammar([A])])
E=noterminal([[4,3],[5]])
A=noterminal([[4,1,E]])
S=noterminal([[1,4],[A]])


#每句
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
    tree = right(S,sentence)
    last_semicolon = current_word

print('s-tree:\n',tree)


# print(tree)
