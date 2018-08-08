from tkinter import *
import tkinter as tk
import AdjacencyListClass
from AdjacencyListClass import WrongNodeError
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from SampleGraph import adjacencyList
from tkinter import messagebox


class CreateObject:
    def __init__(self):
        self.listInstance = AdjacencyListClass.AdjacencyListGraph()
        self.listInstance.adjacencyList = {key: value for (key, value) in adjacencyList.items()}


class MainWindow(Frame, CreateObject):
    def __init__(self):
        Frame.__init__(self)
        CreateObject.__init__(self)
        self.master.title("Railway Connections")
        self.master.geometry("400x350")
        self.master.rowconfigure(7, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.grid(sticky=W + E + N + S)
        self.inputLabel = Label(self, text="Input values:", font=' helvetica 10 bold').grid(row=0, column=0)
        self.optionsLabel = Label(self, text="Available options:", font=' helvetica 10 bold').grid(row=0, column=1)
        self.nodeEntry = Entry(self, textvariable=StringVar(value="Enter one node here (starting city e.g. Suwalki)"),
                               foreground="grey")
        self.nodeEntry.grid(row=1, column=0, sticky=W + E + N + S)
        self.nodeEntry.bind("<Button-1>", self.ClearText)
        self.nodeButton = Button(self, text="Add Node to list", command=self.AddNode, height=1, width=15) \
            .grid(row=1, column=1)
        self.edgesEntry = Entry(self, textvariable=StringVar(value="Enter edges here (e.g. Krakow Rzeszow) "),
                                foreground="grey")
        self.edgesEntry.grid(row=2, column=0, sticky=W + E + N + S)
        self.edgesEntry.bind("<Button-1>", self.ClearText)
        self.edgesButton = Button(self, text="Add Edges to Node", command=self.AddEdges, height=1, width=15)
        self.edgesButton.grid(row=2, column=1)
        self.edgesButtonInfo = CreateTip(self.edgesButton, "dziala")
        self.emptyLabel = Label(self, text="").grid(row=3, column=0)
        self.emptyLabel = Label(self, text="").grid(row=4, column=0)
        self.removeButton = Button(self, text="Remove Node", command=self.RemoveNode, height=1, width=15) \
            .grid(row=3, column=1)
        self.displayButton = Button(self, text="Current Connections", command=self.ShowConnections, height=1, width=15) \
            .grid(row=5, column=1)
        self.clearButton = Button(self, text="Clear Box", command=lambda: self.scrolledText.delete(1.0, END), height=1,
                                  width=15).grid(row=6, column=1)
        self.scrolledText = ScrolledText(self, height=10, width=30)
        self.scrolledText.grid(row=6, column=0)
        self.removeConnectionButton = Button(self, text="Remove Connection", command=self.RemoveConnection, height=1,
                                             width=15).grid(row=4, column=1)
        self.listButton = Button(self, text="Connect Cities", command=AdjListFrameDisplay, height=1, width=12) \
            .grid(row=7, column=0)

    def ShowConnections(self):
        self.scrolledText.insert(INSERT, self.listInstance.displayGraph())

    def AddNode(self):
        try:
            self.listInstance.addNode(self.nodeEntry.get())
        except Exception as e:
            messagebox.showerror("Error", "%s" % e.args)
        else:
            messagebox.showinfo("Information","Node %s added to list" % self.nodeEntry.get())

    def AddEdges(self):
        try:
            self.listInstance.addEdges(self.nodeEntry.get(), self.edgesEntry.get())
        except WrongNodeError as e:
            messagebox.showerror("Error", "No node '%s' in list !" % e.value)
        else:
            messagebox.showinfo("Information", "Edges %s added to node %s" % (self.edgesEntry.get(),
                                                                              self.nodeEntry.get()))

    def RemoveNode(self):
        try:
            self.listInstance.removeNode(self.nodeEntry.get())
        except KeyError as e:
            messagebox.showerror("Error", "No node '%s' in list !" % e.args)
        else:
            messagebox.showinfo("Information", "Node '%s' removed successfully :)" % self.nodeEntry.get())

    def RemoveConnection(self):
        try:
            self.listInstance.removeConnection(self.nodeEntry.get(), self.edgesEntry.get())
        except KeyError as e:
            messagebox.showerror("Error", "No node '%s' in list !" % e.args)
        except ValueError as e:
            messagebox.showerror("Error", "No edge in list !")
        else:
            messagebox.showinfo("Information", "Connection removed successfully :)")


    def ClearText(self, event):
        event.widget.delete(0, END)
        event.widget.config(foreground="black")


class AdjListWindow(CreateObject):
    def __init__(self):
        CreateObject.__init__(self)
        self.top = Toplevel()
        self.top.title('Search connection')
        self.top.geometry("290x260")
        self.top.grid()
        self.top.rowconfigure(5, weight=1)
        self.top.columnconfigure(2, weight=1)
        self.startLabel = Label(self.top, text="Start").grid(row=0, column=0, sticky=W + E + N + S)
        self.top.update()
        self.startComboBox = Combobox(self.top, textvariable=StringVar, values=self.ReturnKeys())
        self.startComboBox.grid(row=0, column=1)
        self.destLabel = Label(self.top, text="Destination").grid(row=1, column=0)
        self.destComboBox = Combobox(self.top, textvariable=StringVar, values=self.ReturnKeys())
        self.destComboBox.grid(row=1, column=1)
        self.connectionButton = Button(self.top, text="Connect", command=self.ConnectCities).grid(column=0, row=2,
                                                                                                  sticky=W + E + N + S)
        self.clearButton = Button(self.top, text="Clear Box", command=lambda: self.textScrollbar.delete(1.0, END)) \
            .grid(row=2, column=1, sticky=W + E + N + S)
        self.textScrollbar = ScrolledText(self.top, height=10, width=20)
        self.textScrollbar.grid(row=3, column=1, sticky=W)
        self.backButton = Button(self.top, text="Back", command=lambda: self.top.destroy()).grid(row=4, column=1)

    def ConnectCities(self):
        try:
            self.getStart = self.startComboBox.get()
        except:

        #self.getStart = self.getStart.replace("'", "").replace(",", "").replace("dict_keys([", "").replace("])", "")
        #self.getDest = self.destComboBox.get()
        #self.getDest = self.getDest.replace("'", "").replace(",", "").replace("dict_keys([", "").replace("])", "")
        try:
            self.textScrollbar.insert(INSERT, self.listInstance.shortestPath(self.getStart, self.getDest))
        except WrongNodeError as e:
            messagebox.showerror("Error", "No connection %s in list !" % e.value)

    def ReturnKeys(self):
        return [key for key, value in self.listInstance.adjacencyList.items()]


class CreateTip(object):
    def __init__(self, widget, text="widget info"):
        self.waitTime = 500
        self.wrapLength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waitTime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 35
        y += self.widget.winfo_rooty() + 20

        self.tw = tk.Toplevel(self.widget)

        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background="#ffffff", relief='solid', borderwidth=1,
                         wraplength=self.wrapLength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


def AdjListFrameDisplay():
    newWindowObject = AdjListWindow()


if __name__ == "__main__":
    MainWindow().mainloop()
