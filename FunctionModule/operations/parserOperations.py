import re
from FunctionModule.RegexMultiPattern import RegexMultiPattern
from FunctionModule.functions.functionList import *



def composeNFunctions(functions):
    '''
    Takes a vector of functions, and compose them, from bottom to top.
    :param functions:  vector of functions.
    :return: the resulting function of the composition.
    '''
    if len(functions) == 0:
        raise Exception("it needs to be at least one function.")

    if len(functions) == 1:
        return lambda x: functions[0](x)
    else:
        return lambda x: functions[0](composeNFunctions(functions[1:])(x))


def separateFromFirstAppareance(sFunction, pattern):
    '''
    Takes the pattern and "splits" the string, but only in the first appareance. Works only with
    pears of patters, () [] " ", etc.
    :param sFunction: string.
    :param pattern: the patter to make the split. 
    :return: a tuple of two strings, before/after the pattern, 
    '''

    if len(pattern) > 1:
        raise Exception("pattern must be a character.")

    head = ""
    tail = ""
    firstRoundStop = 0
    tam = len(sFunction)
    for i in range(tam):
        if sFunction[i] == pattern:
            firstRoundStop = i + 1
            break
        head += sFunction[i]

    tail = sFunction[firstRoundStop:tam - 1]

    return head, tail


def separateIntoStringFunctions(stringFunctions):
    '''
    separates a string of functions, into a vector that contains each function.
    i.e. "sin(cos(tg(x)))" to ["sin","cos","tg","x"]
    :param stringFunctions: a string containing a function.
    :return: a vector containing the functions.
    '''

    pat = "(x(\^\d)?)"
    patron = re.compile(pat)
    stringFuncVec = []
    tail = stringFunctions
    head = ""
    while not (patron.match(tail)):
        head, tail = separateFromFirstAppareance(tail, "(")
        stringFuncVec.append(head)
    stringFuncVec.append(tail)
    return stringFuncVec


def fromStringToFunction(string):
    '''
    takes a string, and identifies the associated function.
    :param string: function in string.
    :return: a function.
    '''

    patterns = ["s[ei]n", "cos", "t(a)?g", "[(log)(lg)]", "(x(\^\d)?)"]
    tam = len(patterns)
    functionVector = [sin(), cos(), tg(), log(10)]
    regex = RegexMultiPattern(patterns)
    index = regex.matchingIndex(string)
    if index is None:
        return index
    elif index == tam - 1:
        power = getThePowerOfString(string)
        return xN(power)
    else:
        return functionVector[index]


def fromStringToCompleteFunction(string):
    '''
    takes a vector of string containing functions, and returns the composed function of it.
    :param string: string containing the function.
    :return: a function.
    '''

    stringFunctionVector = separateIntoStringFunctions(string)
    functionVector = [fromStringToFunction(stringFun) for stringFun in stringFunctionVector]
    return composeNFunctions(functionVector)


def getThePowerOfString(string):
    '''
    takes a string with the form of x^a and returns a.
    :param string:
    :return: a number.
    '''
    splited = string.split("^")
    if len(splited) == 1:
        return 1

    return int(splited[1])


def fromVectorOfStringToVectorOfFunctions(vectorOfString):
    functions = [fromStringToCompleteFunction(elem) for elem in vectorOfString]
    return functions


