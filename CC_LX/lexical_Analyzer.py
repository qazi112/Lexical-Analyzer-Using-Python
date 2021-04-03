# DFAs FOR ALL CLASSES OF TOKENS
# DIRECTORY modules/
# Return True ( if accepeted ) else False
from modules.semicolon import semicolonDFA
from modules.punctuations import punctuationDFA
from modules.logicalOp import logicalOpDFA
from modules.arithematic import aropDFA
from modules.relop import relopDFA
from modules.numbers import numDFA
from modules.identifiers import idDFA
from modules.int import intDFA
from modules.elseD import elseDFA
from modules.ifD import ifDFA
from modules.forD import forDFA
from modules.whileD import whileDFA
from modules.stringD import stringDFA
from modules.floatD import floatDFA
# =============================================================

# SYMBOL TABLE 
"""
    no. 1 | arsalan | line 1

"""
symbolTable = {}

# ===============================================================

# NUMBER TABLE
"""
    no. 1 | 20 | line 2

"""
numberTable = {}

# =================================================================
# ERROR TABLE
"""
    no. 1 | NAME | line 2

"""
errorTable = {}
errorno = 0
# =================================================================

# TOKENS
tokens = []

# =================================================================
# RESERVED WORDS
# There is a seperate DFA for each reserevd word
reserved = ["int", "string","String","for","while","if","else","float"]
# Line numbers tracked
lineNo = 0
# Numbers and symbols for refernce in symbol and number tables
numbers = 0
symbols = 0

# ====================================================================
# File opening and reading

with open('test.txt','r') as file: 
    
    # reading each line     
    for line in file: 
        lineNo += 1
        # reading each word         
        for word in line.split(): 
            # Check for reserved words first
            if word.isdigit():
                # digit detected
                res = numDFA(word)
                if res:
                    # print("Accepted By Number DFA")
                    numberTable[numbers] = [int(word),f"Line No :{lineNo}"]
                    # Added to numberTable
                    tk = ("NUM",numbers)
                    tokens.append(tk)
                    # Token Generated
                    numbers += 1
                else:
                    print("Error")

            else:
                if intDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif ifDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif whileDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif forDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif elseDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif stringDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif floatDFA(word):
                    # print("Keyword Detected")
                    symbolTable[symbols] = [word,f"Line No : {lineNo}, RESERVED WORD"]
                    tk = (word,)
                    tokens.append(tk)
                    symbols += 1
                elif semicolonDFA(word):
                    # print("Semicolon Detected")
                    tk = ("SEMC",)
                    tokens.append(tk)
                elif aropDFA(word):
                    # print("Arop Detected")
                    tk = ("arop",word)
                    tokens.append(tk)

                elif relopDFA(word):
                    # print("relational operator")
                    tk = ("relop", word)
                    tokens.append(tk)
                elif logicalOpDFA(word):
                    # print("Logical operator")
                    tk = ("logi", word)
                    tokens.append(tk)
                elif punctuationDFA(word):
                    # print("punctuations")
                    tk = ("punc", word)
                    tokens.append(tk)
                
                else:
                    # Identifiers

                    res = idDFA(word)
                    if res:
                        # print(word)
                        # print("Identifier")
                        symbolTable[symbols] = [word,f"Line No :{lineNo}"]
                        tk = ("id",symbols)
                        tokens.append(tk)
                        symbols += 1
                    else:
                        # Error detected
                        errorTable[errorno] = [word,f"Error in Line : {lineNo}"]
                        errorno += 1

print("=============================================")
print(f"Errors Occured In Program {len(errorTable)} ")
print()
print("Here is the Error List: ")
print(errorTable)
print("==============================")
print("Numbers Table is  Below")
print(numberTable)
print("===========================")
print("Here is The Symbol Table")
print(symbolTable)
print()
print("=======================")
print("Tokens")
print()
for x in tokens:
    print(x)

