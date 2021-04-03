def start(c):
    dfa = 0
    if c == "i" :
        dfa = 1
    else:
        dfa = 4
    
    return dfa
def state1(c):
    dfa = 0
    if c == "n":
        dfa = 2
    else:
        dfa = 4
    return dfa
def state2(c):
    dfa = 0
    if c == "t":
        dfa = 3
    else:
        dfa = 4
    return dfa
def state3(c):
    dfa = 0
    if len(c) != 0:
        dfa = 4
    return dfa
def state4(c):
    return 4
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
        else:
            dfa = 0
    
    if dfa == 3:
        return 1
    else:
        return 0

def intDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False