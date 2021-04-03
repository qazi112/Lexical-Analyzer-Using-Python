def start(c):
    dfa = 0
    if c == "e" :
        dfa = 1
    else:
        # reject
        dfa = 5
    
    return dfa
def state1(c):
    dfa = 0
    if c == "l":
        dfa = 2
    else:
        dfa = 5
    return dfa
def state2(c):
    dfa = 0
    if c == "s":
        dfa = 3
    else:
        dfa = 5
    return dfa
def state3(c):
    dfa = 0
    if c == "e":
        dfa = 4
    else:
        dfa = 5
    return dfa
def state4(c):
    dfa = 0
    if len(c) != 0:
        dfa = 5
    return dfa
def state5(c):
    return 5 
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
        else:
            dfa = 0
    
    if dfa == 4:
        return 1
    else:
        return 0

def elseDFA(string):
    res = result(string)
    if res:
        return True
    else:
       return False