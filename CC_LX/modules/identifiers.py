import re
def start(c):
    dfa = 0
    if c.isdigit():
        dfa = 3
        # reject
        return dfa
    else:
        dfa = 2
        res = bool(re.match("^[A-Za-z_]*$", c))
        if res:
            dfa = 1
        else:
            dfa = 3
    return dfa

def state1(c):
    # if this is string
    dfa = 0
    res = bool(re.match("^[A-Za-z0-9_]*$", c))
    if res:
        dfa = 2
    else:
        dfa = 3
    return dfa
def state2(c):
    dfa = 0
    res = (bool(re.match("^[A-Za-z0-9_]*$", c)))
    if res:
        dfa = 2
    else:
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

    if dfa == 2 or dfa == 1:
        return 1
    else:
        return 0

def idDFA(lexeme):
    res = result(lexeme)
    if res:
        return True
    else:
       return False