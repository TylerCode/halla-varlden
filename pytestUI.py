# A small test/example of making a user interface with Python. Useful especially for 
# the raspberry pi. (When you have half a dozen of the things, you never get bored)


from Tkinter import Tk, RIGHT, BOTH, RAISED
from ttk import Frame, Button, Style


class Taco(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()

        
    def initUI(self):
      
        self.parent.title("Taco Time")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        
        self.pack(fill=BOTH, expand=True)
        
        closeButton = Button(self, text="Close", command=self.quit()) ## NOPE
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK", command=self.quit()) #Surprise Motherf***er!!!
        okButton.pack(side=RIGHT)
              

def main():
  
    root = Tk()
    root.geometry("300x200+300+300")
    app = Taco(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  