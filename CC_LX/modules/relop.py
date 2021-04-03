def start(c):
    dfa = 0
    if c == "<":
        dfa = 1
    elif c == ">":
        dfa = 3
    elif c == "=":
        dfa = 4 
    else:
        # Dead
        dfa = 5
    return dfa

def state1(c):
    
    dfa = 0
    if len(c) == 0:
        dfa = 1
    if c == "=":
        dfa = 2
    else:
        dfa = 4
    return dfa

# Reject State (2)
def state2(c):
    return -1

def state3(c):
    dfa = 0
    if c == "=":
        dfa = 2
    else:
        dfa = 5
    return dfa
def state4(c):
    dfa = 0
    if c == "=":
        dfa = 2
    else:
        dfa = 5
    return dfa

def result(lexeme):
    dfa = 0
    l = len(lexeme)
    for x in range(l):
        if dfa == 0:
     
            dfa = start(lexeme[x])
        elif dfa == 1:
     
            dfa = state1(lexeme[x])
        elif dfa == 3:
            dfa = state3(lexeme[x])
        elif dfa == 4:
            dfa = state4(lexeme[x])        
        elif dfa == 2:
            dfa = state2(lexeme[x])
        else:
            dfa = 0
    
    if dfa == 1 or dfa == 2 or dfa == 3:
        return 1
    else:
        return 0

def relopDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False