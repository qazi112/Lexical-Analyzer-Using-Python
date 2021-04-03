def start(c):
    dfa = 0
    if c == "." or c == "(" or c == ")" or c == "{" or c == "}":
        dfa = 1
    else:
        dfa = 2
    
    return dfa
def state1(c):
    if len(c)!= 0:
        dfa = 2
    else:
        dfa = -1
    return dfa
def state2(c):
    return -1

def result(lexeme):
    dfa = 0
    l = len(lexeme)
    for x in range(l):
        if dfa == 0:

            dfa = start(lexeme[x])
        elif dfa == 1:

            dfa = state1(lexeme[x])
        elif dfa == 2:

            dfa = state2(lexeme[x])
        else:
            dfa = 0

    if dfa == 1:
        return 1
    else:
        return 0

def punctuationDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False