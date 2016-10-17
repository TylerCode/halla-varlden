# A small test/example of making a user interface with Python. Useful especially for 
# the raspberry pi. (When you have half a dozen of the things, you never get bored)

from Tkinter import Tk, Frame, BOTH

class Taco(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
      
        self.parent.title("Taco")
        self.pack(fill=BOTH, expand=1)



def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Taco(root)
    root.mainloop()  


if __name__ == '__main__':
    main()