from tkinter import Tk , Text , END
from tkinter.filedialog import askopenfile , asksaveasfile
from tkinter.messagebox import showerror

root = Tk()
root.title("arnix-textedit")

main = Text(root , font=("Caskaydia Cove Nerd Font" , 12))
main.pack(expand=True , fill="both")

file = None

cfsize = 12

class FileOperations():
    def open():
        global file
        file = askopenfile()
        try:
            cnt = file.read()
            pass
        except UnicodeDecodeError:
            showerror("Error" , "An UnicodeDecodeError occured")
        except AttributeError:
            showerror("Error" , "No file was selected")

        main.delete(1.0 , END)
        main.insert(END , cnt)

    def save_as():
        file = asksaveasfile()
        try:
            file.write(main.get(1.0 , END))
        except AttributeError:
            showerror("Error" , "No fule was detected")

    def save():
        if file==None:
          FileOperations.save_as()
        else:
          file.seek(0)
          contents=main.get(1.0 , END)
          file.write(contents) 
          file.truncate()

class FontSize():
    def increase(event):
        global cfsize
        cfsize = cfsize + 1
        main.configure(font=("Caskaydia Cove Nerd Font" , cfsize))
    
    def decrease(event):
        global cfsize
        cfsize = cfsize - 1
        main.configure(font=("Caskaydia Cove Nerd Font" , cfsize))

root.bind("<Control-o>" , lambda event:FileOperations.open())
root.bind("<Control-s>" , lambda event:FileOperations.save())
root.bind("<Control-Shift-S>" , lambda event:FileOperations.save_as())
root.bind("<Control-y>" , lambda event:main.edit_redo())
root.bind("<Control-z>" , lambda event:main.edit_undo())
root.bind('<Control-Shift-plus>' , FontSize.increase)
root.bind('<Control-minus>' , FontSize.decrease)


if __name__ == "__main__":
    root.mainloop()
