import SolverModule.operations.solverOperations as op
import SolverModule.operations.matrixOperations as mt


class SEL:
    def __init__(self, x, y, functions, constants=None):

        self.matA, self.matB, self.matC, self.funct = self.__buildMatrices(x, y, functions, constants)
        self.X = x
        self.Y = y
        self.solution = []
        self.error = None
        self.completeFunction = None

    def __buildMatrices(self, x, y, f, C=None):
        '''
        Takes x elements, y elements and FunctionModule element, and builds two matrices,
        A and B of the system A.C=B
        :param x: vector of x elements
        :param y: vector of y elements
        :param f: vector of function
        :return: matrices A and B, of the system A.C = B
        '''

        N = len(f)
        M = len(x)

        ##############
        # Creating the R matrix, where each column is the result of
        # applying each function (f) to x
        ##############
        R = mt.zeroes(M, N)

        for i in range(N):
            columna = op.applyFunctionToX(f[i], x)
            mt.copyVectorToColumn(R, i, columna)

        ##############
        # Creating A and B as zeros matrices.
        ##############
        A = mt.zeroes(N)
        B = mt.zeroes(N, 1)

        for i in range(N):
            B[i] = mt.scalarProduct(mt.column(R, i), y)
            for j in range(N):
                A[i][j] = mt.scalarProduct(mt.column(R, i), mt.column(R, j))

        # Creating C matrix.
        if C is None:
            C = ["C" + str(e) for e in range(N)]

        return A, B, C, f

    def pivot(self, type='total'):

        '''


        :param type: indicates the kind of pivot ("total" or "partial")
        :return: Explanation String.
        '''

        resultString = ""  ############################# --E--

        if op.needsPivote(self.matA):

            ##############
            # Determinar el tipo de pivoteo.
            ##############
            totalPivot = True
            if type == 'partial':
                totalPivot = False
            elif type != "total":
                raise Exception("no such type of pivot")

            ##############
            # Realizar el pivote.
            ##############
            if totalPivot:
                resultString += op.totalPivot(self.matA, self.matC, self.matB,
                                              self.funct)  ############################# --E--
            else:
                resultString += op.partialPivot(self.matA, self.matC, self.matB,
                                                self.funct)  ############################# --E--

            resultString += mt.systemToString(self.matA,self.matC,self.matB)
        else:
            resultString += "\nNo requiere Pivoteo\n"

        return resultString

    def triangulate(self):
        '''
        Triangulates the matrices.
        :return:
        '''
        resultString = ""
        resultString += op.triangulate(self.matA, self.matC, self.matB)
        return resultString

    def substitution(self):

        self.solution = op.sustitution(self.matA, self.matB)
        self.completeFunction = op.createFunction(self.solution, self.funct)
        self.error = op.calculateError(self.X, self.Y, self.completeFunction)

    def getA(self):
        return mt.matToString(self.matA, "A")

    def getB(self):
        return mt.vectToString(self.matB, "B")

    def getC(self):
        return mt.vectToString(self.matC, "C")

    def getSystem(self):
        return mt.systemToString(self.matA, self.matC, self.matB, "A", "C", "B")

    def getSolution(self):
        return mt.twoEqualedMatricesToString(self.matC, self.solution)

    def getSolutionVector(self):
        return self.solution

    def getError(self):
        return "\nError = \t" + str(self.error)

    def getCompleteFunction(self):
        return self.completeFunction
