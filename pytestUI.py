# A small test/example of making a user interface with Python. Useful especially for 
# the raspberry pi. (When you have half a dozen of the things, you never get bored)

from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style

class Taco(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("Tacos for days")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=5, y=5)


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Taco(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  