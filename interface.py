from tkinter import *
import tkinter.ttk
import avl

title = "AVL Tree Implementation"
subtitle = "Data Structure II Homework for UFPI / 2018.1"

class MainMenu(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title(title)
        # Criação do Container Mestre
        self.top = Frame(self.master)
        self.top.pack()
        self.topLabel = Label(self.top, text=title+',\n'+subtitle)
        self.topLabel.pack()

        # Criação da Toolbar


        # Toolbar File: [Ler do Arquivo | Sobre]

        # Criação da Lista de Nós (treeview)
        self.treeviewcontainer = Frame(self.top)
        # tree = ttk.Treeview(self.treeviewcontainer)
        tree = tkinter.ttk.Treeview(self.treeviewcontainer)
        tree["columns"] = ("key", "data")
        tree.column("key", width=100)
        tree.column("data", width=300)
        tree.heading("key", text="Chave")
        tree.heading("data", text="Lista de Dados")

        self.insertNodeIntoListView(tree, avl.Node(15, ["penes", "viadinho"]))

        id2 = tree.insert("", 1, "dir2", text="Dir 2")
        tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))

        ##alternatively:
        tree.insert("", 3, "dir3", text="Dir 3")
        tree.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))

        tree.pack()
        self.treeviewcontainer.pack()

        # Criação da Textbox
        self.nodeControlContainer = Frame(self.master)
        self.nodeTextBoxLabel = Label(self.nodeControlContainer, text="Node value: ")
        self.nodeTextBox = Text(self.nodeControlContainer, height=1, width=40)
        self.nodeTextBoxLabel.pack(side=LEFT)
        self.nodeTextBox.pack(side=LEFT)


        # Criação dos Botões
        # Container dos botões
        self.buttonsContainer = Frame(self.master)

        # Botão Inserir
        self.insertButton = Button(self.buttonsContainer, text="Inserir nó")
        self.insertButton["width"] = 20
        self.insertButton.pack(side=LEFT)
        # Botão Remover
        self.removeButton = Button(self.buttonsContainer, text="Remover nó")
        self.removeButton["width"] = 20
        self.removeButton.pack(side=LEFT)
        # Botão Mostrar
        self.showButton = Button(self.buttonsContainer, text="Mostrar nó")
        self.showButton["width"] = 20
        self.showButton.pack(side=LEFT)

        # Criação da Debug Bar


        #Packing
        self.buttonsContainer.pack(side=BOTTOM)
        self.nodeControlContainer.pack(side=BOTTOM)


    ### Funções para cada botão

    def insertButton_function(self):
        pass
    def removeButton_function(self):
        pass
    def showButton_function(self):
        pass

    ### Funções-auxílio para cada botão

    def insertNodeIntoListView(self, tree, node):
        if node is not None:
            tree.insert("", 0, text="Nó "+ str(node.key), values=(str(node.key), str(node.data)))
            pass
    def find_traverseViaDirectory(self, tree, key):
        tree.column
        pass