def start(c):
    dfa = 0
    if c == "i" :
        dfa = 1
    else:
        # reject
        dfa = 3
    
    return dfa
def state1(c):
    dfa = 0
    if c == "f":
        dfa = 2
    else:
        dfa = 3
    return dfa
def state2(c):
    dfa = 0
    if len(c) != 0:
        dfa = 3
    return dfa
def state3(c):
    return 3
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
        
        else:
            dfa = 0
    
    if dfa == 2:
        return 1
    else:
        return 0

def ifDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False