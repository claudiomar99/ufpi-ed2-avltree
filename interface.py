from tkinter import *

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

        # Criação da Textbox
        self.nodeControlContainer = Frame(self.master)
        self.nodeTextBoxLabel = Label(self.nodeControlContainer, text="Node value: ")
        self.nodeTextBox = Text(self.nodeControlContainer, height=1)
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