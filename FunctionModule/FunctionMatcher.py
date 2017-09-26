from FunctionModule.functions.functionList import *
import re


class FunctionMatcher():
    def __init__(self, pattern, functions):
        self.pattern = pattern
        self.functions = functions

    def match(self, functionString):
        pat = re.compile(self.pattern)
        if pat.match(functionString):
            return self.functions
        return None
