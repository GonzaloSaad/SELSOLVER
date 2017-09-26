from tkinter import *
from tkinter.scrolledtext import ScrolledText

from ConvertersModule.ToTXT import StringToTXTConverter as toTXT
from SolverModule import SelSolverCore as sel
from GrapherModule import Plotter as plt


class SolverGUI:
    def __init__(self, masterRoot):
        # Getting the sizes of the window.
        self.textResolution = ""
        self.cantSolved = 0
        self.completeFunction = None
        self.setSize(masterRoot)
        self.setMasterConfig(masterRoot)
        self.createMenues(masterRoot)
        self.createFrames(masterRoot)
        self.createTextboxes(self.topRigthFrame)
        self.createButtons(self.topRigthFrame)
        self.createLabel(self.topRigthFrame)
        self.createScrolledText(self.bottomFrame)

    # Metodo para arrancar el programa.
    def run(self):
        self.master.mainloop()

    # Metodo para determinar los tamaños que se utilizaran.
    def setSize(self, master):
        self.Height = master.winfo_screenheight() // 2
        self.Width = master.winfo_screenwidth() // 2

    # Metodo para configurar el master (root) de la aplicacion.
    def setMasterConfig(self, master):
        master.resizable(width=True, height=True)
        master.minsize(0, self.Height)
        self.master = master

    # Metodo para crear los frames.
    def createFrames(self, master):
        h = self.Height
        w = self.Width

        self.topFrame = Frame(master, height=h * 0.9, width=w, highlightbackground="black", highlightcolor="black",
                              highlightthickness=1)
        self.topFrame.pack(side=TOP, fill=BOTH, expand=True)

        self.bottomFrame = Frame(master, height=h * 0.1, width=w, highlightbackground="black",
                                 highlightcolor="black",
                                 highlightthickness=1)
        self.bottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.topLeftFrame = Frame(self.topFrame, height=h * 0.8, width=w * 0.6, highlightbackground="black",
                                  highlightcolor="black", highlightthickness=1)
        self.topLeftFrame.pack(side=LEFT, fill=BOTH, expand=True)

        self.topRigthFrame = Frame(self.topFrame, height=h * 0.8, width=w * 0.4, highlightbackground="black",
                                   highlightcolor="black", highlightthickness=1)
        self.topRigthFrame.pack(side=LEFT, fill=BOTH, expand=True)

    # Metodo para crear menues.
    def createMenues(self, master):
        # Crear menu principal.
        self.menuPrincipal = Menu(master)

        # Agregar menu principal al master.
        self.master.config(menu=self.menuPrincipal)

        # Crear submenu de opciones
        self.subMenuOpciones = Menu(self.menuPrincipal, tearoff=False)
        self.menuPrincipal.add_cascade(label="Opciones", menu=self.subMenuOpciones)

    # Metodo para crear botones.
    def createButtons(self, master):
        master.update()
        w = master.winfo_width()  # width
        h = master.winfo_height()  # height
        xButton = w * 0.1
        yButton = h * 0.1 + 150
        self.buttonAceptar = Button(master, text="Aceptar")
        self.buttonAceptar.bind("<Button-1>", self.buttonAceptarClick)
        self.buttonAceptar.place(x=xButton, y=yButton)

        self.buttonGuardar = Button(master, text="Guardar")
        self.buttonGuardar.bind("<Button-1>", self.buttonSaveClick)
        self.buttonGuardar.place(x=xButton + 60, y=yButton)

    # Metodo para crear labels.
    def createLabel(self, master):
        master.update()
        w = master.winfo_width()  # width
        h = master.winfo_height()  # height
        xLabel = w * 0.05
        yLabel = h * 0.9

        self.labelFunction = Label(master, text="<<Funcion>>")
        self.labelFunction.place(x=xLabel, y=yLabel)

    # Metodo para crear Textbox.
    def createTextboxes(self, master):
        master.update()
        w = master.winfo_width()  # width
        h = master.winfo_height()  # height

        xLabelX = w * 0.01
        yLabelX = h * 0.20

        self.labelX = Label(master, text="X: ")
        self.labelX.place(x=xLabelX, y=yLabelX)

        self.labelY = Label(master, text="Y: ")
        self.labelY.place(x=xLabelX, y=yLabelX + 30)

        self.labelF = Label(master, text="F: ")
        self.labelF.place(x=xLabelX, y=yLabelX + 60)

        self.txtX = Entry(master, width=30)
        self.txtX.place(x=xLabelX + 50, y=yLabelX)

        self.txtY = Entry(master, width=30)
        self.txtY.place(x=xLabelX + 50, y=yLabelX + 30)

        self.txtF = Entry(master, width=40)
        self.txtF.place(x=xLabelX + 50, y=yLabelX + 60)

    def createScrolledText(self, master):
        self.scrollTxt = ScrolledText(master, undo=True)
        self.scrollTxt['font'] = ('consolas', '12')
        self.scrollTxt.pack(expand=True, fill='both')

    def createScrolledText2(self, master):
        self.txt = Text(master, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        scrollb = Scrollbar(master, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set

    def buttonAceptarClick(self, event):
        x, y, f = self.__readTextboxes()

        text, fun = self.__solve(x, y, f)
        self.__setText(text)
        self.__plot(x, y, fun)

        self.cantSolved += 1

    def buttonSaveClick(self, event):
        txtSaver = toTXT.StringToTXTConverter()
        txtSaver.write(self.textResolution, "res" + str(self.cantSolved).rjust(4, "0"))

    def __solve(self, x, y, f):
        sel_Solver = sel.SelSolverCore(x, y, f)
        text = sel_Solver.solve()
        fun = sel_Solver.getCompleteFunction()
        return text, fun

    def __plot(self, x, y, f):
        plot = plt.Plotter(x, y, f)
        plot.plot()

    def __setText(self, textToSet):
        self.scrollTxt.delete("1.0", END)
        self.scrollTxt.insert(INSERT, textToSet)

    def __readTextboxes(self):
        x = [int(elem) for elem in self.txtX.get().split(",")]
        y = [int(elem) for elem in self.txtY.get().split(",")]
        f = self.txtF.get()
        return x, y, f
