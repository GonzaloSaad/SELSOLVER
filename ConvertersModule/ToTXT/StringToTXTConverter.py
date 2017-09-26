from tkinter.filedialog import asksaveasfile
from tkinter import Tk


class StringToTXTConverter:
    def write(self, textToConvert, fileName):

        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing

        filename = asksaveasfile(mode="w",
                                 defaultextension=".txt",
                                 filetypes=[("Archivo de Texto", ".txt")],
                                 title="Guardar Resolucion",
                                 confirmoverwrite=True,
                                 initialfile=fileName
                                 )  # show an "Open" dialog box and return the path to the selected file
        if filename is None:
            return
        try:
            filename.write(textToConvert)
        except Exception as e:
            raise Exception("the file did not save")
