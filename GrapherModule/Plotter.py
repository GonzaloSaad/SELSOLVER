import matplotlib.pyplot as plt



class Plotter:
    def __init__(self,x,y,f):
        self.F = f
        self.X=x
        self.Xf=self.__createLineNumber(min(x),max(x),0.1)
        self.Y=y
        self.Yf=[f(el) for el in self.Xf]


    def plot(self):
        plt.scatter(self.X,self.Y)
        plt.plot(self.Xf,self.Yf)
        plt.show()



    def __createLineNumber(self,start, stop, step):
        res = []
        num = start
        while num <= stop:
            res.append(num)
            num += step
        return res
