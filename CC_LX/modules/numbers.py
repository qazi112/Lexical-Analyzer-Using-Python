def start(c):
    dfa = 0
    if c.isdigit():
        c = int(c)
    else:
        dfa = 2
        return dfa
    if c in range(0,10):
        dfa = 1
    else:
        dfa = 2   
    return dfa
def state1(c):
    # if this is string
    if c.isdigit():
        c = int(c)    
    else:
        dfa = 2
        return dfa

    if c in range(0,10):
        dfa = 1
    else:
        dfa = 2
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

def numDFA(num):
    res = result(num)
    if res:
        return True
    else:
       return False