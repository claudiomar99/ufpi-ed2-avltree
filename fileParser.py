import avl
import json

class FileParser:

    def __init__(self, file):
        self.list = []
        # Converte os dados do arquivo para uma lista de AVL_NODEs
    def getList(self):
        try:
            arquivo = open('input.txt', 'r')
            file = arquivo.read()
            string = file[file.index("{"):]
            self.list = json.loads(string)
            arquivo.close()
        except:
            pass
        return self.list
