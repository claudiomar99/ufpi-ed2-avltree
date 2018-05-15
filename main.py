import tkinter
import interface
import avl
import fileParser

node = avl.Node(15, [])
print(node)

main = tkinter.Tk()
interface.MainMenu(main)
main.option_add('*tearOff', False)
main.mainloop()

