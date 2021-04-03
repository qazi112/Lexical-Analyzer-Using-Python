def start(c):
    dfa = 0
    if c == "f" :
        dfa = 1
    else:
        # reject
        dfa = 6
    return dfa
def state1(c):
    dfa = 0
    if c == "l":
        dfa = 2
    else:
        dfa = 6
    return dfa
def state2(c):
    dfa = 0
    if c == "o":
        dfa = 3
    else:
        dfa = 6
    return dfa
def state3(c):
    dfa = 0
    if c == "a":
        dfa = 4
    else:
        dfa = 6
    return dfa
def state4(c):
    dfa = 0
    if c == "t":
        dfa = 5
    else:
        dfa = 6
    return dfa
def state5(c):
    dfa = 0
    if len(c) != 0:
        dfa = 6
    return dfa
def state6(c):
    return 6

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
        elif dfa == 3:
            
            dfa = state3(lexeme[x])
        elif dfa == 4:
            dfa = state4(lexeme[x])
        elif dfa == 5:
            dfa = state5(lexeme[x])
        elif dfa == 6:
            dfa = state6(lexeme[x])
        else:
            dfa = 0

    if dfa == 5:
        return 1
    else:
        return 0

def floatDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False