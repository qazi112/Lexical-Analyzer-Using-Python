def start(c):
    dfa = 0
    if c == "s" or c == "S" :
        dfa = 1
    else:
        # reject
        dfa = 7
    
    return dfa
def state1(c):
    dfa = 0
    if c == "t":
        dfa = 2
    else:
        dfa = 7
    return dfa
def state2(c):
    dfa = 0
    if c == "r":
        dfa = 3
    else:
        dfa = 7
    return dfa
def state3(c):
    dfa = 0
    if c == "i":
        dfa = 4
    else:
        dfa = 7
    return dfa
def state4(c):
    dfa = 0
    if c == "n":
        dfa = 5
    else:
        dfa = 7
    return dfa

def state5(c):
    dfa = 0
    if c == "g":
        dfa = 6
    else:
        dfa = 7
    return dfa

def state6(c):
    dfa = 0
    if len(c) != 0:
        dfa = 7
    return dfa
def state7(c):
    return 7
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
        elif dfa == 7:
            dfa = state7(lexeme[x])    
        else:
            dfa = 0
    
    if dfa == 6:
        return 1
    else:
        return 0

def stringDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False