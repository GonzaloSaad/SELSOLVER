import FunctionModule.FunctionEntryParser as fp
import SolverModule.SEL as sel


class SelSolverCore:
    def __init__(self, x, y, function):
        parser = fp.FunctionEntryParser(function)
        self.functions = parser.getFunctions()
        self.constants = parser.getConstants()
        self.x = x
        self.y = y
        self.solution = []
        self.completeFunction=None

    def solve(self):
        explanation = "\n________________________SOLUCION________________________\n"

        selSolver = sel.SEL(self.x, self.y, self.functions, self.constants)

        explanation += "\n----------------------- MATRICES -----------------------\n"

        explanation += selSolver.getSystem()

        explanation += "\n----------------------- PIVOTEO  -----------------------\n"

        explanation += selSolver.pivot("total")

        explanation += "\n--------------------- TRIANGULACION --------------------\n"

        explanation += selSolver.triangulate()

        explanation += "\n---------------------- SUSTITUCION ---------------------\n"

        selSolver.substitution()
        explanation += selSolver.getSolution()
        explanation += selSolver.getError()

        self.solution=selSolver.getSolutionVector()
        self.completeFunction = selSolver.getCompleteFunction()
        return explanation

    def getCompleteFunction(self):
        return self.completeFunction


