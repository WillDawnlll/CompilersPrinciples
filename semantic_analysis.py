# coding=utf-8
word_type=('integer','float','operator')
compute=[('a', 5,'integer'), ('=', 3,'operator'), [('a', 4,'integer'), ('*', 3,'operator'), [('b', 4,'integer'), ('+', 3,'operator'), [[('2', 5,'integer')]]]]]

A=[[4,3,'A'],['E']]
E=[[4],[5]]

a=[['integer','operator','integer'],['integer']]

check_stack=['integer','operator','integer']

def check(sen):
    for word in sen:
        if type(word) is list:
            check_stack.pop()
            if len(word) == 3:
                check_stack.extend(a[0])
            elif len(word) == 1:
                check_stack.extend(a[1])
            w = check(word)
            if w is False:
                return False
            else:
                check_stack.append(w)
                sen[sen.index(word)]=[0,0,w]

        if sen.index(word) == len(sen)-1:
            while True:
                if len(sen) == 0:
                    return 'integer'
                else:
                    if sen.pop()[2] is not check_stack.pop():
                        return False

print(str(check(compute)))
