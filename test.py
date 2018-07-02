# coding=utf-8
class noterminal(list):
    def __init__(self,l):
        self.list=l
E=noterminal([[4,3],[5]])
A=noterminal([[4,1,E]])
S=noterminal([[1,4],[A]])

len(S)
print(len(S))
print(type(S))
print('l',len(list(S)))
print(type(S))

def p(tr):
    print(str(tr))
    for gra in non.list:
        for gram in  gra:
            if gram is noterminal:
                p(gram)
            else:
                print(non)
