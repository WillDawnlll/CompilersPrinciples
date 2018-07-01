# coding=utf-8

from lexical_analysis import word_stream

#语法树，文法，非终结符
class tree(list):
    def __init__(self,l):
        self.list=l
class grammar(list):
    def __init__(self,l):
        self.list=l
class noterminal(list):
    def __init__(self,l):
        self.list=l


#检测文法和句子是否匹配
#只考虑右递归
def right(t_grammar, t_sentence):
    for seq in range(0, len(t_grammar) - 1):
        #当前词序号对应的文法词为非终结符
        if t_grammar[seq] is noterminal:
            #，从此非终结符的文法表中查找
            for tt_grammar in t_grammar[seq]:
                #某文法首词,同当前词序号对应的句子词相同
                if tt_grammar[0] == t_sentence[seq]:
                    #当前词序到结尾的句子替换为相应多一层数组的return子句
                    tt_sentence = t_sentence[seq:-1]
                    t_sentence.pop(seq,-1)
                    result = right(tt_grammer, tt_sentence)
                    if result == False:
                        return False
                    else:
                        return t_sentence.append(result)
        else:
            if t_sentence[seq][1] == t_grammar[seq]:
                if seq == len(t_grammar)-1:
                    return t_sentence
            else:
                return False


#定义文法
E=noterminal([grammar([4,3]),grammar([5])])
A=noterminal([grammar([4,1,E]))
S=noterminal([grammar([1,4]),grammar([A])])

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
    print(sentence)
    tree = right(S,sentence)
    last_semicolon = current_word


# print(tree)
