import tkinter
import interface
import avl
import fileParser

# Permite o acesso direto
node = avl.Node(15, [])
print(node)

main = tkinter.Tk()
interface.MainMenu(main)
# Opção para permitir a criação de uma menubar no Windows.
main.option_add('*tearOff', False)
main.mainloop()

