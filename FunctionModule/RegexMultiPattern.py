import re


class RegexMultiPattern():
    def __init__(self, patternsToParse):
        self.patterns = patternsToParse

    def matchingIndex(self, stringTo):

        for i in range(len(self.patterns)):
            regex = re.compile(self.patterns[i])
            if regex.match(stringTo):
                return i

        return None
   