import FunctionModule.operations.parserOperations as po


class FunctionEntryParser:
    def __init__(self, stringOfFunctions):
        self.constants, stringFunc = self.__separateFunctionFromConstants(stringOfFunctions)
        self.functions = po.fromVectorOfStringToVectorOfFunctions(stringFunc)

    def __separateFunctionFromConstants(self, funString):
        '''
        takes a function string, separates in terms, and then separates in products.
        :param funString: a function in string.
        :return: two vectors, one of constants, other of string functions.
        '''

        term = funString.split("+")
        termCant = len(term)

        const = [None] * termCant
        func = [None] * termCant
        aux = [None] * 2
        aux[0] = const
        aux[1] = func

        for i in range(termCant):
            prod = term[i].split("*")
            for j in range(len(prod)):
                aux[j][i] = prod[j].strip()

        for i in range(termCant):
            if func[i] is None:
                func[i] = "x^0"

        return const, func



    def getConstants(self):
        return self.constants

    def getFunctions(self):
        return self.functions


